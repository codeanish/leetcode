from maximum_product_subarray_0152 import main

def test_hello():
    assert main.hello() == "Hello"

def test_maximum_product_subarray():
    assert main.maximum_product_subarray([2,3,-2,4]) == 6
    assert main.maximum_product_subarray([2,3,-2,8]) == 8
    assert main.maximum_product_subarray([-2,0,-1]) == 0
    assert main.maximum_product_subarray([2,2,2,0,2,3,2,0,2,2,2]) == 12
    assert main.maximum_product_subarray([-2,5,-2,0,4,4,4,0,0,1,2,3]) == 64
    assert main.maximum_product_subarray([-2]) == -2
    assert main.maximum_product_subarray([-2,-2]) == 4