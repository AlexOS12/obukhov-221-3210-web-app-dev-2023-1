import subprocess
import pytest

INTERPRETER = 'python'

def run_script(filename, input_data=None):
    proc = subprocess.run(
        [INTERPRETER, filename],
        input='\n'.join(input_data if input_data else []),
        capture_output=True,
        text=True,
        check=False
    )
    return proc.stdout.strip()

test_data = {
    'python_if_else': [
        ('1', 'Weird'),
        ('4', 'Not Weird'),
        ('3', 'Weird'),
        ('6','Weird'),
        ('22', 'Not Weird')
    ],
    'arithmetic_operators': [
        (['1', '2'], ['3', '-1', '2']),
        (['10', '5'], ['15', '5', '50'])
    ],
    'division' : [
        (['5', '4'], ['1', '1.25']),
        (['0', '2'], ['0', '0.0']),
        (['5', '0'], ['Нельзя делить на ноль!'])
    ],
    'loops' : [
        ('3', ['0', '1', '4']),
        ('1', ['0']),
        ('20', ['0', '1', '4', '9', '16', '25', '36', '49', '64', '81', '100', '121', '144', '169', '196', '225', '256', '289', '324', '361'])
    ],
    'print_function' : [
        ('5', ['12345']),
        ('0', ['']),
        ('20', ['1234567891011121314151617181920'])
    ],
    'second_score' : [
        (['5', '2 3 6 6 5'], ['5']),
        (['2', '1 1'], ['1']),
        (['10', '1 2 3 4 5 5 4 3 2 1'], ['4'])
    ],
    'nested_list' : [
        (['5', 'Гарри', '37.21', 'Берри', '37.21','Тина', '37.2','Акрити', '41','Харош', '39'], ['Берри', 'Гарри']),
        (['2', 'Гарри', '37.21', 'Берри', '48'], ['Берри']),
        (['5', 'Гарри', '10', 'Берри', '10','Тина', '10','Акрити', '10','Харош', '10'], ['Акрити', 'Берри', 'Гарри', 'Тина', 'Харош'])
    ],
    'lists' : [
        (['4', 'append 1', 'append 2', 'insert 1 3', 'print'], ['[1, 3, 2]']),
        (['0'], ['']),
        (['12',
          'insert 0 5',
          'insert 1 10',
          'insert 0 6',
          'print',
          'remove 6',
          'append 9',
          'append 1',
          'sort',
          'print',
          'pop',
          'reverse',
          'print'],
          ['[6, 5, 10]',
           '[1, 5, 9, 10]',
           '[9, 5, 1]'])
    ],
    'swap_case' : [
        ('Www.MosPolytech.ru', ['wWW.mOSpOLYTECH.RU']),
        ('Pythonist 2', ['pYTHONIST 2']),
        ('', [''])
    ],
    'split_and_join' : [
        ('this is a string', ['this-is-a-string']),
        ('hello-world and bye!', ['hello-world-and-bye!']),
        ('', [''])
    ]
}

def test_hello_world():
    assert run_script('hello_world.py') == 'Hello, world!'

@pytest.mark.parametrize("input_data, expected", test_data['python_if_else'])
def test_python_if_else(input_data, expected):
    assert run_script('python_if_else.py', [input_data]) == expected

@pytest.mark.parametrize("input_data, expected", test_data['arithmetic_operators'])
def test_arithmetic_operators(input_data, expected):
    assert run_script('arithmetic_operators.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['division'])
def test_division(input_data, expected):
    assert run_script('division.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['loops'])
def test_loops(input_data, expected):
    assert run_script('loops.py', [input_data]).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['print_function'])
def test_print_function(input_data, expected):
    assert run_script('print_function.py', [input_data]).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['second_score'])
def test_second_score(input_data, expected):
    assert run_script('second_score.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['nested_list'])
def test_nested_list(input_data, expected):
    assert run_script('nested_list.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['lists'])
def test_list(input_data, expected):
    assert run_script('lists.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['swap_case'])
def test_list(input_data, expected):
    assert run_script('swap_case.py', [input_data]).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['split_and_join'])
def test_list(input_data, expected):
    assert run_script('split_and_join.py', [input_data]).split('\n') == expected

def test_max_word():
    assert run_script('max_word.py') == 'сосредоточенности'

def test_price_sum():
    assert run_script('price_sum.py') == '6842.84 5891.06 6810.90'