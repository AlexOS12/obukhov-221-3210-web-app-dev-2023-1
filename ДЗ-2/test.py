import subprocess
import pytest

INTERPRETER = 'python'

def run_script(filename, input_data=None, argv=None):
    proc = subprocess.run(
        [INTERPRETER, filename, *argv],
        input='\n'.join(input_data if input_data else []),
        capture_output=True,
        text=True,
        check=False
    )
    return proc.stdout.strip()

test_data = {
    'fact' : [
        (1, 1),
        (5, 120),
        (8, 40320),
        (100, 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000)
    ],
    'show_employee' : [
        (("Иванов Иван Иванович", 10_000), "Иванов Иван Иванович: 10000 ₽"),
        (("Иванов Иван Иванович",), "Иванов Иван Иванович: 100000 ₽")
    ],
    'sum_and_sub' : [
        ((5, 3), (8, 2)),
        ((1, 1), (2, 0)),
        ((1111, 2222), (3333, -1111))
    ],
    'process_list' : [
        ([1, 2, 3, 4, 5], [1, 4, 27, 16, 125]),
        ([], [])
    ],
    'my_sum' : [
        ((1, 2, 3, 4), 10.0),
        (tuple(), 0.0)
    ],
    'my_sum_argv' : [
        (['1', '2', '3', '4'], '10.0'),
        ([], '0.0')
    ],
    'file_search' : [
        ('file_search_test.txt', ['1', '2', '3', '4', '5']),
        ('notExistingFile.txt', 'Файл notExistingFile.txt не найден')
    ]
}

from fact import fact_it, fact_rec

@pytest.mark.parametrize("input_data, expected", test_data['fact'])
def test_fact_it(input_data, expected):
    assert fact_it(input_data) == expected

@pytest.mark.parametrize("input_data, expected", test_data['fact'])
def test_fact_rec(input_data, expected):
    assert fact_rec(input_data) == expected

from show_employee import show_employee

@pytest.mark.parametrize("input_data, expected", test_data['show_employee'])
def test_show_employee(input_data, expected):
    assert show_employee(*input_data) == expected

from sum_and_sub import sum_and_sub

@pytest.mark.parametrize("input_data, expected", test_data['sum_and_sub'])
def test_sum_and_sub(input_data, expected):
    assert sum_and_sub(*input_data) == expected

from process_list import process_list_comp, process_list_gen

@pytest.mark.parametrize("input_data, expected", test_data['process_list'])
def test_process_list_comp(input_data, expected):
    assert process_list_comp(input_data) == expected

@pytest.mark.parametrize("input_data, expected", test_data['process_list'])
def test_process_list_gen(input_data, expected):
    test_list = list(process_list_gen(input_data))
    assert test_list == expected

from my_sum import my_sum

@pytest.mark.parametrize("input_data, expected", test_data['my_sum'])
def test_pmy_sum(input_data, expected):
    assert my_sum(*input_data) == expected

@pytest.mark.parametrize("input_data, expected", test_data['my_sum_argv'])
def test_my_sum_argv(input_data, expected):
    assert run_script("my_sum_argv.py", argv=input_data) == expected

@pytest.mark.parametrize("input_data, expected", test_data['file_search'])
def test_file_search(input_data, expected):
    assert run_script("file_search.py", argv=input_data)