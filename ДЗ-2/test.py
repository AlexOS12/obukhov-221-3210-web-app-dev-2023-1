from plane_angle import plane_angle, Point
from average_scores import compute_average_scores
from my_sum import my_sum
from process_list import process_list_comp, process_list_gen
from sum_and_sub import sum_and_sub
from show_employee import show_employee
from fact import fact_it, fact_rec
from phone_number import sort_phone
from people_sort import name_format
from circle_square_mk import circle_square_mk
import subprocess
import pytest

INTERPRETER = 'python'


def run_script(filename, input_data=None, argv=None):
    if not (argv):
        argv = []

    proc = subprocess.run(
        [INTERPRETER, filename, *argv],
        input='\n'.join(input_data if input_data else []),
        capture_output=True,
        text=True,
        check=False
    )
    return proc.stdout.strip()


test_data = {
    'fact': [
        (1, 1),
        (5, 120),
        (6, 720),
        (8, 40320),
        (100, 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000)
    ],
    'show_employee': [
        (("Иванов Иван Иванович", 10_000), "Иванов Иван Иванович: 10000 ₽"),
        (("Иванов Иван Иванович",), "Иванов Иван Иванович: 100000 ₽")
    ],
    'sum_and_sub': [
        ((5, 3), (8, 2)),
        ((1, 1), (2, 0)),
        ((1.23, 2.25), (3.48, -1.02)),
        ((1111, 2222), (3333, -1111))
    ],
    'process_list': [
        ([1, 2, 3, 4, 5], [1, 4, 27, 16, 125]),
        ([], []),
        ([997, 998, 999], [991026973, 996004, 997002999])
    ],
    'my_sum': [
        ((1, 2, 3, 4), 10.0),
        (tuple(), 0.0),
        ((1,), 1.0),
        ((1234.56, 2545.78, 3.45), 3783.79),
        ((10, -9), 1.0)
    ],
    'my_sum_argv': [
        (['1', '2', '3', '4'], '10.0'),
        ([], '0.0'),
        (['1'], '1.0'),
        (['1234.56', '2545.78', '3.45'], '3783.79'),
        (['10', '-9'], '1.0')
    ],
    'file_search': [
        (['file_search_test.txt'], ['1', '2', '3', '4', '5']),
        (['notExistingFile.txt'], ['Файл notExistingFile.txt не найден']),
        ([''], ['Файл  не найден'])
    ],
    'email_validation': [
        (['3',
         'lara@mospolytech.ru',
          'brian-23@gmail.com',
          'britts_24@yandex.ru'],
         "['brian-23@gmail.com', 'britts_24@yandex.ru', 'lara@mospolytech.ru']"),
        (['3',
         'aboba@gmail.com',
          'cucumber.com',
          'tomato@mail'],
         "['aboba@gmail.com']"),
        (['3',
          'ab#ba@mail.ru',
          'aboba@@mail.ru',
          'aboba@mail..ru'],
         "[]"),
        (['2',
          'aboba@mail.ru',
          'ABOBA@MAIL.RU'],
         "['ABOBA@MAIL.RU', 'aboba@mail.ru']"),
        (['2',
          'aboba@mail.sosiska',
          'aboba@mail.ru'],
          "['aboba@mail.ru']")
    ],
    'fibonacci': [
        ('1', '[0]'),
        ('5', '[0, 1, 1, 8, 27]'),
        ('9', '[0, 1, 1, 8, 27, 125, 512, 2197, 9261]'),
        (['10'], '[0, 1, 1, 8, 27, 125, 512, 2197, 9261, 39304]')
    ],
    'compute_avg_scores': [
        (([89, 90, 78, 93, 80],
         [90, 91, 85, 88, 86],
         [91, 92, 83, 89, 90.5]),
         (90.0, 91.0, 82.0, 90.0, 85.5)),
        (([]),
         ())
    ],
    'plane_angle': [
        ((Point(0, 0, 0), Point(1, 1, 1), Point(1, 0, 0), Point(0, 0, 1)),
         35.26438968275466),
        ((Point(1, 2, 3), Point(6, 5, 4), Point(7, 8, 9), Point(6, 5, 7)),
         49.79703411343024),
    ],
    'phones': [
        ((7895462130, 89875641230, 9195969878),
         ["+7 (789) 546-21-30",
          "+7 (919) 596-98-78",
          "+7 (987) 564-12-30"]),
        ((), [])
    ],
    'people_sort': [
        ((['Mike', 'Thomson', '20', 'M'], ['Robert', 'Bustle', '32', 'M'],
          ['Andria', 'Bustle', '30', 'F']),
         ['Mr. Mike Thomson',
          'Ms. Andria Bustle',
          'Mr. Robert Bustle']),
        (([]), []),
        ((['Mike', 'Thomson', '20', 'M'], ['Robert', 'Bustle', '20', 'M'],
          ['Andria', 'Bustle', '20', 'F']),
         ['Mr. Mike Thomson',
          'Mr. Robert Bustle',
          'Ms. Andria Bustle']),
        ((['Mike', 'Thomson', '20', 'M'], ['Mike', 'Thomson', '40', 'M'],
          ['Mike', 'Thomson', '30', 'M']),
         ['Mr. Mike Thomson',
          'Mr. Mike Thomson',
          'Mr. Mike Thomson']),
    ],
    'complex_numbers': [
        (['2 1', '5 6'],
         "['7.00+7.00i', '-3.00-5.00i', '4.00+17.00i', '0.26-0.11i', '2.24+0.00i', '7.81+0.00i']"),
        (['1 2', '3 4'],
         "['4.00+6.00i', '-2.00-2.00i', '-5.00+10.00i', '0.44+0.08i', '2.24+0.00i', '5.00+0.00i']"),
        (['1.23 4.56', '7.89 0.12'],
         "['9.12+4.68i', '-6.66+4.44i', '9.16+36.13i', '0.16+0.58i', '4.72+0.00i', '7.89+0.00i']"),

    ],
    'circle_square_mk': [
        ((1, 1000), 3.14),
        ((5, 1000), 78.54),
        ((0, 0), 0),
        ((-10, -5), 0),
        ((200, 10000), 125663.71)
    ]
}


@pytest.mark.parametrize("input_data, expected", test_data['fact'])
def test_fact_it(input_data, expected):
    assert fact_it(input_data) == expected


@pytest.mark.parametrize("input_data, expected", test_data['fact'])
def test_fact_rec(input_data, expected):
    assert fact_rec(input_data) == expected


@pytest.mark.parametrize("input_data, expected", test_data['show_employee'])
def test_show_employee(input_data, expected):
    assert show_employee(*input_data) == expected


@pytest.mark.parametrize("input_data, expected", test_data['sum_and_sub'])
def test_sum_and_sub(input_data, expected):
    assert sum_and_sub(*input_data) == expected


@pytest.mark.parametrize("input_data, expected", test_data['process_list'])
def test_process_list_comp(input_data, expected):
    assert process_list_comp(input_data) == expected


@pytest.mark.parametrize("input_data, expected", test_data['process_list'])
def test_process_list_gen(input_data, expected):
    test_list = list(process_list_gen(input_data))
    assert test_list == expected


@pytest.mark.parametrize("input_data, expected", test_data['my_sum'])
def test_my_sum(input_data, expected):
    assert my_sum(*input_data) == expected


@pytest.mark.parametrize("input_data, expected", test_data['my_sum_argv'])
def test_my_sum_argv(input_data, expected):
    assert run_script("my_sum_argv.py", argv=input_data) == expected


@pytest.mark.parametrize("input_data, expected", test_data['file_search'])
def test_file_search(input_data, expected):
    assert run_script("file_search.py", argv=input_data).split(
        '\n') == expected


@pytest.mark.parametrize("input_data, expected", test_data['email_validation'])
def test_email_validation(input_data, expected):
    assert run_script("email_validation.py", input_data=input_data) == expected


@pytest.mark.parametrize("input_data, expected", test_data['fibonacci'])
def test_fibonacci(input_data, expected):
    assert run_script("fibonacci.py", input_data=input_data) == expected


@pytest.mark.parametrize("input_data, expected", test_data['compute_avg_scores'])
def test_compute_avg_scores(input_data, expected):
    assert compute_average_scores(input_data) == expected


@pytest.mark.parametrize("input_data, expected", test_data['plane_angle'])
def test_plane_angle(input_data, expected):
    assert plane_angle(*input_data) == expected


@pytest.mark.parametrize("input_data, expected", test_data['phones'])
def test_phones(input_data, expected):
    assert sort_phone(input_data) == expected


@pytest.mark.parametrize("input_data, expected", test_data['people_sort'])
def test_people_sort(input_data, expected):
    assert name_format(input_data) == expected


@pytest.mark.parametrize("input_data, expected", test_data['complex_numbers'])
def test_complex_numbers(input_data, expected):
    assert run_script("complex_numbers.py", input_data=input_data) == expected


@pytest.mark.parametrize("input_data, expected", test_data['circle_square_mk'])
def test_circle_square_mk(input_data, expected):
    # Допустимая погрешность 5%
    ideal = expected
    low, high = ideal * 0.95, ideal * 1.05
    assert low <= circle_square_mk(*input_data) <= high
