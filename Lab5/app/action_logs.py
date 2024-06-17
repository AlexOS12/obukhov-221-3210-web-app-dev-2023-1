import math
import io
from flask import Blueprint,  render_template, request, send_file
from flask_login import current_user, login_required
from app import db_connector
from authorization import can_user
from mysql.connector.errors import DatabaseError


logs_bp = Blueprint('logs', __name__, url_prefix='/logs')

PAGE_COUNT = 10

def generate_file(fields, records):
    result = ','.join(fields) + '\n'
    for record in records:
        line = ','.join([str(getattr(record, field, '') or '') for field in fields]) + '\n'
        result += line 
    return io.BytesIO(result.encode())

@logs_bp.route('/')
def index():
    logs = []
    page_number = request.args.get('page_number', 1, type = int)
    
    try:
        db_connection = db_connector.connect()
        with db_connection.cursor(named_tuple=True) as cursor:
            query_main = ("SELECT visit_logs.id, users.login, visit_logs.path, visit_logs.created_at "
                     "FROM visit_logs LEFT JOIN users ON visit_logs.user_id = users.id ")
            query_filter = ""

            if current_user.is_authenticated:
                if current_user.is_admin():
                    query_filter = ""
                else:
                    query_filter = f"WHERE user_id = {current_user.id} "
            else:
                query_filter = "WHERE user_id is NULL "

            query_order = (
                     "ORDER BY visit_logs.id DESC "
                     f"LIMIT {PAGE_COUNT} OFFSET {PAGE_COUNT*(page_number - 1)} ")
            

            query = query_main + query_filter + query_order

            print(31)
            cursor.execute(query)
            logs = cursor.fetchall()

            query = ("SELECT COUNT(*) as count FROM visit_logs")
            cursor.execute(query)
            total_count = cursor.fetchone().count
            all_page = math.ceil(total_count / PAGE_COUNT)
            start_page = max(page_number - 2, 1)
            end_page = min(page_number + 2, all_page)

            return render_template("action_logs.html", logs=logs, start_page=start_page, end_page=end_page, page_number=page_number)
    except DatabaseError as error:
        print(f"Произошла ошибка БД: {error}")

@logs_bp.route('/users_stat')
@login_required
@can_user('view_users_stat')
def users_stat():
    logs = []    
    page_number = request.args.get('page_number', 1, type = int)
    try:
        db_connection = db_connector.connect()
        with db_connection.cursor(named_tuple=True) as cursor:
            if request.args.get('download'):
                query = ("SELECT users.login, COUNT(*) as visit_count "
                         "FROM visit_logs LEFT JOIN users on visit_logs.user_id = users.id "
                         "GROUP BY users.id "
                         "ORDER BY visit_count desc ")
                cursor.execute(query)
                logs = cursor.fetchall()
                file = generate_file(['login', 'visit_count'], logs)
                return send_file(file, mimetype='text/csv', as_attachment=True, download_name='user_stat.csv')
                
            query = ("SELECT users.login, COUNT(*) as visit_count "
            "FROM visit_logs LEFT JOIN users on visit_logs.user_id = users.id "
            "GROUP BY users.id "
            "ORDER BY visit_count desc "
            f"LIMIT {PAGE_COUNT} OFFSET {PAGE_COUNT*(page_number - 1)}" )
            cursor.execute(query)
            logs = cursor.fetchall()

            query = ("SELECT COUNT(*) as count from (SELECT DISTINCT user_id from visit_logs) as uniq_users")
            cursor.execute(query)
            total_count = cursor.fetchone().count

            all_page = math.ceil(total_count / PAGE_COUNT)
            start_page = max(page_number - 2, 1)
            end_page = min(page_number + 2, all_page)


            return render_template("users_stat.html", logs=logs, start_page=start_page, end_page=end_page, page_number=page_number)
    except DatabaseError as error:
        print(f"Произошла ошибка БД: {error}")    


@logs_bp.route('/pages_stat')
@login_required
@can_user('view_pages_stat')
def pages_stat():
    logs = []
    page_number = request.args.get('page_number', 1, type = int)

    try:
        db_connection = db_connector.connect()
        with db_connection.cursor(named_tuple=True) as cursor:
            if request.args.get('download'):
                query = ("SELECT path, COUNT(*) as visit_count from visit_logs "
                        "group by path "
                        "order by visit_count desc, path " )
                cursor.execute(query)
                logs = cursor.fetchall()
                file = generate_file(['path', 'visit_count'], logs)
                return send_file(file, mimetype='text/csv', as_attachment=True, download_name='pages_stat.csv')
                
            query = ("SELECT path, COUNT(*) as visit_count from visit_logs "
                     "group by path "
                     "order by visit_count desc, path "
                     f"LIMIT {PAGE_COUNT} OFFSET {PAGE_COUNT*(page_number - 1)}"
            )
            cursor.execute(query)
            logs = cursor.fetchall()

            query = ("SELECT COUNT(*) as count from (SELECT DISTINCT path from visit_logs) as uniq_paths")
            cursor.execute(query)
            total_count = cursor.fetchone().count

            all_page = math.ceil(total_count / PAGE_COUNT)
            start_page = max(page_number - 2, 1)
            end_page = min(page_number + 2, all_page)


            return render_template("pages_stat.html", logs=logs, start_page=start_page, end_page=end_page, page_number=page_number)
    except DatabaseError as error:
        print(f"Произошла ошибка БД: {error}")

    return render_template("logs_base.html")

    