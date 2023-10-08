from src import main

def test_hello():
    assert main.hello() == "Hello"

def test_largest_subarray_sum_n2():
    assert main.largest_subarray_sum_n2([-2,1,-3,4,-1,2,1,-5,4]) == 6
    assert main.largest_subarray_sum_n2([1]) == 1
    assert main.largest_subarray_sum_n2([1,1]) == 2
    assert main.largest_subarray_sum_n2([1,-1,1,1,-5,1]) == 2
    assert main.largest_subarray_sum_n2([5,4,-1,7,8]) == 23
    assert main.largest_subarray_sum_n2([-1]) == -1
    assert main.largest_subarray_sum_n2([-2,-1]) == -1
    assert main.largest_subarray_sum_n2([-2,-1,-1,-3]) == -1
    assert main.largest_subarray_sum_n2([-2,-1,-1,1,-3]) == 1

def test_largest_subarray_sum():
    assert main.largest_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]) == 6
    assert main.largest_subarray_sum([1]) == 1
    assert main.largest_subarray_sum([1,1]) == 2
    assert main.largest_subarray_sum([1,-1,1,1,-5,1]) == 2
    assert main.largest_subarray_sum([5,4,-1,7,8]) == 23
    assert main.largest_subarray_sum([-1]) == -1
    assert main.largest_subarray_sum([-2,-1]) == -1
    assert main.largest_subarray_sum([-2,-1,-1,-3]) == -1
    assert main.largest_subarray_sum([-2,-1,-1,1,-3]) == 1