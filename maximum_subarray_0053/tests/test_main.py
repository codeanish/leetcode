from maximum_subarray_0053 import main

def test_hello():
    assert main.hello() == "Hello"

def test_largest_subarray_sum_n2():
    assert main.largest_subarray_sum_n2([-2,1,-3,4,-1,2,1,-5,4]) == 6
    assert main.largest_subarray_sum_n2([1]) == 1
    assert main.largest_subarray_sum_n2([1,1]) == 2
    assert main.largest_subarray_sum_n2([1,-1,1,1,-5,1]) == 2
    assert main.largest_subarray_sum_n2([5,4,-1,7,8]) == 23

def test_largest_subarray_sum():
    assert main.largest_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]) == 6
    assert main.largest_subarray_sum([1]) == 1
    assert main.largest_subarray_sum([1,1]) == 2
    assert main.largest_subarray_sum([1,-1,1,1,-5,1]) == 2
    assert main.largest_subarray_sum([5,4,-1,7,8]) == 23
