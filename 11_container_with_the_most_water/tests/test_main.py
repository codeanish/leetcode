from src import main

def test_hello():
    assert main.hello() == "Hello"

def test_max_area_unitary_elements():
    assert main.max_area([1,1]) == 1
    assert main.max_area([1,1,1]) == 2
    assert main.max_area([1,1,1,1]) == 3
    assert main.max_area([1,1,1,1,1]) == 4
    assert main.max_area([1,1,1,1,1,1]) == 5

def test_max_area_test_case_1():
    assert main.max_area([1,8,6,2,5,4,8,3,7]) == 49
