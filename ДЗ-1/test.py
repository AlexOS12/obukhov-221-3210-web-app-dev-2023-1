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
        (['10', '5'], ['15', '5', '50']),
        (['0', '0'], ['0', '0', '0'])
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
        (['10', '1 2 3 4 5 5 4 3 2 1'], ['4']),
        (['7', '-5 8 4 3 5 2 7'], ['7'])
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
    ],
    'anagram' : [
        (['hello', 'elhol'], ['YES']),
        (['Hello', 'hello'], ['YES']),
        (['automobile', 'vehicle'], ['NO'])
    ],
    'metro' : [
        (['3', 
          '10', '15',
          '20', '30',
          '15', '25',
          '15'], ['2']),
        (['2',
          '10', '20',
          '20', '30',
          '20'], ['2']),
        (['3',
          '10', '15',
          '20', '25',
          '10', '25',
          '30'], ['0'])
    ], 
    'minion_game' : [
        ('BANANA', ['Стюарт 12']),
        ('BBB', ['Стюарт 6']),
        ('AAA', ['Кевин 6']),
        ('SOMERANDOMWORD', ['Стюарт 63'])
    ],
    'is_leap' : [
        ('1900', ['False']),
        ('2000', ['True']),
        ('2004', ['True']),
        ('2025', ['False'])
    ],
    'happiness' : [
        (['3 2',
          '1 5 3',
          '3 1',
          '5 7'], ['1']),
        (['4 4',
          '1 2 3 4',
          '1 2 3 4',
          '6 7 8 9'], ['4']),
        (['3 3',
          '1 2 3',
          '4 5 6',
          '1 2 3'], ['-3'])
    ],
    'pirate_ship' : [
        (['10 4',
          'a 4 10',
          'b 5 9',
          'c 1 2',
          'd 3 3'],
          ['a 4 10',
           'c 1 2',
           'b 5 9']),
        (['5 2',
          'a 3 3',
          'b 4 3'],
          ['a 3 3',
           'b 2 1.50']),
        (['100 2',
          'a 10 100',
          'b 100 90'],
          ['a 10 100',
           'b 90 81']),
        (['1 1',
          'a 50 10'],
          ['a 1 0.20'])
    ],
    'mat_mult' : [
        (['2',
         '1 2', 
         '3 4',
         '5 6',
         '7 8'],
         ['19 22',
          '43 50']),
        (['3',
          '1 2 3',
          '4 5 6',
          '7 8 9',
          '9 8 7',
          '6 5 4',
          '3 2 1'],
          ['30 24 18',
           '84 69 54',
           '138 114 90']),
        (['4',
          '1 1 1 1',
          '2 2 2 2',
          '3 3 3 3',
          '4 4 4 4',
          '5 5 5 5',
          '6 6 6 6',
          '7 7 7 7',
          '8 8 0 8'],
          ['26 26 18 26',
           '52 52 36 52',
           '78 78 54 78',
           '104 104 72 104'])
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
def test_swap_case(input_data, expected):
    assert run_script('swap_case.py', [input_data]).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['split_and_join'])
def test_split_and_join(input_data, expected):
    assert run_script('split_and_join.py', [input_data]).split('\n') == expected

def test_max_word():
    assert run_script('max_word.py') == 'сосредоточенности'

def test_price_sum():
    assert run_script('price_sum.py') == '6842.84 5891.06 6810.90'

@pytest.mark.parametrize("input_data, expected", test_data['anagram'])
def test_anagram(input_data, expected):
    assert run_script('anagram.py', input_data).split('\n') == expected 

@pytest.mark.parametrize("input_data, expected", test_data['metro'])
def test_metro(input_data, expected):
    assert run_script('metro.py', input_data).split('\n') == expected 

@pytest.mark.parametrize("input_data, expected", test_data['minion_game'])
def test_minion_game(input_data, expected):
    assert run_script('minion_game.py', [input_data]).split('\n') == expected 

@pytest.mark.parametrize("input_data, expected", test_data['is_leap'])
def test_is_leap(input_data, expected):
    assert run_script('is_leap.py', [input_data]).split('\n') == expected    

@pytest.mark.parametrize("input_data, expected", test_data['happiness'])
def test_happiness(input_data, expected):
    assert run_script('happiness.py', input_data).split('\n') == expected    

@pytest.mark.parametrize("input_data, expected", test_data['pirate_ship'])
def test_pirate_ship(input_data, expected):
    assert run_script('pirate_ship.py', input_data).split('\n') == expected    

@pytest.mark.parametrize("input_data, expected", test_data['mat_mult'])
def test_mat_mult(input_data, expected):
    assert run_script('matrix_mult.py', input_data).split('\n') == expected    