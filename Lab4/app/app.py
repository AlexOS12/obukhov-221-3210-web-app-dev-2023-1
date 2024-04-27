from flask import Flask, render_template, session, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required
from mysqldb import DBConnector
from mysql.connector.errors import DatabaseError
from pyScripts import pass_checker


app = Flask(__name__)
application = app
app.config.from_pyfile("config.py")

db_connector = DBConnector(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth"
login_manager.login_message = "Войдите, чтобы просматривать содержимое данной страницы"
login_manager.login_message_category = "warning"


class User(UserMixin):
    def __init__(self, user_id, login):
        self.id = user_id
        self.login = login


def get_user_list():
    return [{"user_id": "14", "login": "root", "password": "admin"},
            {"user_id": "64", "login": "guest", "password": "c1sc0"},
            {"user_id": "98", "login": "user", "password": "example"}]


CREATE_USER_FIELDS = ["login", "password", "last_name",
                      "first_name", "middle_name", "role_id"]
EDIT_USER_FIELDS = ["last_name", "first_name", "mid_name", "role_id"]
PASS_CHANGE_FIELDS = ["old_pass", "new_pass", "new_pass_confirm"]


def get_roles():
    query = "SELECT * FROM roles"

    with db_connector.connect().cursor(named_tuple=True) as cursor:
        cursor.execute(query)
        roles = cursor.fetchall()
    return roles


@login_manager.user_loader
def load_user(user_id):
    query = "SELECT id, login FROM users WHERE id=%s"

    with db_connector.connect().cursor(named_tuple=True) as cursor:

        cursor.execute(query, (user_id,))

        user = cursor.fetchone()

    if user:
        return User(user_id, user.login)

    return None


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/info")
def info():
    session["counter"] = session.get("counter", 0) + 1

    return render_template("info.html")


@app.route("/auth", methods=["GET", "POST"])
def auth():
    if request.method == "GET":
        return render_template("auth.html")

    login = request.form.get("login", "")
    password = request.form.get("pass", "")
    remember = request.form.get("remember") == "on"

    query = "SELECT id, login FROM users WHERE login=%s AND pass_hash=SHA2(%s, 256)"

    print(query)

    with db_connector.connect().cursor(named_tuple=True) as cursor:

        cursor.execute(query, (login, password))

        print(cursor.statement)

        user = cursor.fetchone()

    if user:
        login_user(User(user.id, user.login), remember=remember)
        flash("Успешная авторизация", category="success")
        target_page = request.args.get("next", url_for("index"))
        return redirect(target_page)

    flash("Введены некорректные учётные данные пользователя", category="danger")

    return render_template("auth.html")


@app.route("/users")
def users():
    query = "SELECT users.*, roles.name as role_name FROM users LEFT JOIN roles ON users.role_id = roles.id"

    with db_connector.connect().cursor(named_tuple=True) as cursor:
        cursor.execute(query)
        data = cursor.fetchall()

    return render_template("users.html", users=data)


def get_form_data(required_fields):
    user = {}

    for field in required_fields:
        user[field] = request.form.get(field) or None

    return user


@app.route("/user/<int:user_id>/view")
def view_user(user_id):

    query = ("SELECT users.*, roles.name "
             "FROM users JOIN roles on users.role_id = roles.id "
             f"WHERE users.id = {user_id} LIMIT 1")
    
    try:
        with db_connector.connect().cursor(named_tuple=True) as cursor:
            cursor.execute(query)
            user = cursor.fetchone()
            
            if not user:
                flash(f"Пользователь с id={user_id} не найден", category="danger")
                return redirect(url_for("users"))
            
            return render_template("view_user.html", user=user)

    except DatabaseError as error:
        flash(f"Не удалось получить информацию о пользователе {error}", category="danger")
        return render_template("view_user.html")

@app.route("/users/<int:user_id>/edit", methods=["GET", "POST"])
@login_required
def edit_user(user_id):
    query = "SELECT * FROM users where id = %s"
    roles = get_roles()
    with db_connector.connect().cursor(named_tuple=True) as cursor:
        cursor.execute(query, (user_id, ))
        user = cursor.fetchone()

    if request.method == "POST":
        user = get_form_data(EDIT_USER_FIELDS)
        user["user_id"] = user_id
        query = ("UPDATE users "
                 "SET last_name=%(last_name)s, first_name=%(first_name)s, "
                 "mid_name=%(mid_name)s, role_id=%(role_id)s "
                 "WHERE id=%(user_id)s ")

        try:
            with db_connector.connect().cursor(named_tuple=True) as cursor:
                cursor.execute(query, user)
                db_connector.connect().commit()

            flash("Запись пользователя успешно обновлена", category="success")
            return redirect(url_for("users"))
        except DatabaseError as error:
            flash(
                f"Ошибка редактирования пользователя! {error}", category="danger")
            db_connector.connect().rollback()

    return render_template("edit_user.html", user=user, roles=roles)


@app.route("/user/<int:user_id>/delete", methods=["POST"])
@login_required
def delete_user(user_id):
    query = "DELETE FROM users WHERE id=%s"

    try:
        with db_connector.connect().cursor(named_tuple=True) as cursor:
            cursor.execute(query, (user_id, ))
            db_connector.connect().commit()

        flash("Запись пользователя успешно удалена", category="success")
    except DatabaseError as error:
        flash(f"Ошибка удаления пользователя! {error}", category="danger")
        db_connector.connect().rollback()

    return redirect(url_for("users"))


@app.route("/users/new", methods=["GET", "POST"])
@login_required
def create_user():
    user = {}
    roles = get_roles()
    if request.method == "POST":
        user = get_form_data(CREATE_USER_FIELDS)

        query = ("INSERT INTO users "
                 "(login, pass_hash, last_name, first_name, mid_name, role_id) "
                 "VALUES (%(login)s, SHA2(%(password)s, 256), "
                 "%(last_name)s, %(first_name)s, %(middle_name)s, %(role_id)s)")
        try:
            with db_connector.connect().cursor(named_tuple=True) as cursor:
                cursor.execute(query, user)
                db_connector.connect().commit()
            return redirect(url_for("users"))
        except DatabaseError as error:
            flash(f"Ошибка создания пользователя! {error}", category="danger")
            db_connector.connect().rollback()

    return render_template("user_form.html", user=user, roles=roles)


@app.route("/change_pass", methods=("GET", "POST"))
@login_required
def change_pass():

    if request.method == "GET":
        return render_template("change_pass.html")

    pass_form = get_form_data(PASS_CHANGE_FIELDS)
    pass_form.update({"user_id": current_user.id})

    try:
        old_pass_check_query = ("SELECT pass_hash = SHA2(%(old_pass)s, 256) as check_result "
                                "from users where id = %(user_id)s LIMIT 1")
        change_pass_query = ("UPDATE users "
                             "SET pass_hash = SHA2(%(new_pass)s, 256) "
                             "WHERE id = %(user_id)s")

        with db_connector.connect().cursor(named_tuple=True) as cursor:
            cursor.execute(old_pass_check_query, pass_form)
            old_pass_check_result = cursor.fetchone()

            if not int(old_pass_check_result.check_result):
                flash("Введен неверный старый пароль!", category="warning")
                return render_template("change_pass.html")
            if pass_form["new_pass"] != pass_form["new_pass_confirm"]:
                flash("Новые пароли не совпадают!", category="warning")
                return render_template("change_pass.html")

            new_pass_check, new_pass_check_comment = pass_checker.check_pass(
                pass_form["new_pass"])

            if not new_pass_check:
                flash(new_pass_check_comment, category="warning")
                return render_template("change_pass.html")

            cursor.execute(change_pass_query, pass_form)
            db_connector.connect().commit()

            flash("Пароль успешно сменён!", category="success")
            return redirect(url_for("index"))

    except DatabaseError as error:
        flash(f"Не удалось сменить пароль! {error}", category="danger")
        db_connector.connect().rollback()

    return redirect(url_for("index"))


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/secret")
@login_required
def secret():
    return render_template("secret.html")

# python -m venv ve
# . ve/bin/activate -- Linux
# ve\Scripts\activate -- Windows
# pip install flask python-dotenv
