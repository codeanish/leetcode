from search_in_rotated_sorted_array_0033 import main

def test_hello():
    assert main.hello() == "Hello"

def test_search_in_rotated_sorted_array_single_element():
    assert main.search_array([1], 1) == 0

def test_search_in_rotated_sorted_array_two_elements():
    assert main.search_array([1,2], 1) == 0
    assert main.search_array([2,1], 1) == 1

def test_search_in_rotated_sorted_array_three_elements():
    assert main.search_array([1,2,3], 1) == 0
    assert main.search_array([3,1,2], 1) == 1
    assert main.search_array([2,3,1], 1) == 2

def test_search_in_rotated_sorted_array_5_elements():
    assert main.search_array([1,2,3,4,5],2) == 1
    assert main.search_array([5,1,2,3,4],2) == 2
    assert main.search_array([4,5,1,2,3],2) == 3
    assert main.search_array([3,4,5,1,2],2) == 4
    assert main.search_array([2,3,4,5,1],2) == 0
    assert main.search_array([2,3,4,6,1],6) == 3
    assert main.search_array([2,3,4,6,1],5) == -1
    assert main.search_array([8,123,1,5,7],100) == -1
    assert main.search_array([8,123,1,5,7],4) == -1
    assert main.search_array([8,123,1,5,7],8) == 0
    assert main.search_array([8,123,1,5,7],123) == 1
    assert main.search_array([8,123,1,5,7],1) == 2
    assert main.search_array([8,123,1,5,7],5) == 3
    assert main.search_array([8,123,1,5,7],7) == 4
