from product_of_array_except_self_0238 import main

def test_hello():
    assert main.hello() == "Hello"

def test_product_except_self():
    assert main.product_except_self([1,2,3,4]) == [24,12,8,6]
    assert main.product_except_self([-1,1,0,-3,3]) == [0,0,9,0,0]