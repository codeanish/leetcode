from random import randint
from find_minimum_in_rotated_sorted_array_0153 import main

def test_hello():
    assert main.hello() == "Hello"

# def test_split_array_at_midpoint_with_minimum():
    # assert main.split_array_at_midpoint_with_minimum([11,13,15,17]) == [11,13]

def test_find_minimum_in_rotated_sorted_array_1():
    assert main.find_minimum([11,13,15,17]) == 11

def test_find_minimum_in_rotated_sorted_array_5():
    assert main.find_minimum([17,11,13,15]) == 11

def test_find_minimum_in_rotated_sorted_array_2():
    assert main.find_minimum([3,4,5,1,2]) == 1

def test_find_minimum_in_rotated_sorted_array_3():
    assert main.find_minimum([4,5,6,7,0,1,2]) == 0

def test_find_minimum_in_rotated_sorted_array_4():
    assert main.find_minimum([7,0,1,2,4,5,6]) == 0

def test_find_minimum_in_rotated_sorted_array_5():
    assert main.find_minimum([8,9,10,0,1,2,3,4,5,6,7]) == 0



    # 0,1,2,3,4,5,6,7,8,9,10
    # 8,9,10,0,1,2,3,4,5,6,7