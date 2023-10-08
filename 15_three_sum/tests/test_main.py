import pytest
from srd import main

def test_hello():
    assert main.hello() == "Hello"

# def test_three_sum_array_too_small():
#     nums = [1]
#     with pytest.raises(Exception):
#         main.three_sum(nums)

# def test_three_sum_array_too_big():
#     nums = range(3001)
#     with pytest.raises(Exception):
#         main.three_sum(nums)

def test_three_sum_three_elements_sums_to_zero():
    nums = [0,0,0]
    assert main.three_sum(nums) == [[0,0,0]]

def test_three_sum_4_elements_sums_to_zero():
    nums = [0,0,0,0]
    assert main.three_sum(nums) == [[0,0,0]]

def test_three_sum_three_elements_no_zero_sum():
    nums = [0,1,1]
    assert main.three_sum(nums) == []

def test_extra_test_cases():
    nums = [-1,0,1,0]
    assert main.three_sum(nums) == [[-1,0,1]]