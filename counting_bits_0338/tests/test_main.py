from counting_bits_0338 import main

def test_hello():
    assert main.hello() == "Hello"

def test_counting_bits_0():
    assert main.counting_bits(0) == [0]

def test_counting_bits_1():
    assert main.counting_bits(1) == [0,1]

def test_counting_bits_2():
    assert main.counting_bits(2) == [0,1,1]

def test_counting_bits_3():
    assert main.counting_bits(3) == [0,1,1,2]

def test_counting_bits_4():
    assert main.counting_bits(4) == [0,1,1,2,1]

def test_counting_bits_5():
    assert main.counting_bits(5) == [0,1,1,2,1,2]


def test_counting_bits_6():
    assert main.counting_bits(6) == [0,1,1,2,1,2,2]