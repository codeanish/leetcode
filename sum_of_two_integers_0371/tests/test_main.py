from sum_of_two_integers_0371 import main

def test_get_sum_example_1_not_in_spirit():
    a = 1
    b = 2
    assert main.get_sum_not_in_the_spirit(a, b) == 3


def test_get_sum_example_2_not_in_spirit():
    a = 2
    b = 3
    assert main.get_sum_not_in_the_spirit(a, b) == 5


def test_get_sum_1_plus_1_equals_2():
    a = 1
    b = 1
    assert main.get_sum(a, b) == 2

def test_get_sum_example_1():
    a = 1
    b = 2
    assert main.get_sum(a, b) == 3

def test_get_sum_example_2():
    a = 2
    b = 3
    assert main.get_sum(a, b) == 5

def test_get_sum_minus_1_plus_1_equals_0():
    a = -1
    b = 1
    assert main.get_sum(a, b) == 0

def test_get_sum_minus_1_plus_0_equals_minus_1():
    a = -1
    b = 0
    assert main.get_sum(a, b) == -1

def test_get_sum_minus1_minus_1_equals_minus_2():
    a = -1
    b = -1
    assert main.get_sum(a, b) == -2

def test_big_minus():
    a = -1000
    b = -1000
    assert main.get_sum(a, b) == -2000

def test_big_addition():
    a = 1000
    b = 1000
    assert main.get_sum(a, b) == 2000

def test_big_addition_zero():
    a = -1000
    b = 1000
    assert main.get_sum(a, b) == 0