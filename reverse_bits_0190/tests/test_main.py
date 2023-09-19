from reverse_bits_0190 import main

def test_hello():
    assert main.hello() == "Hello"

def test_reverse_bits_example_1():
    input_integer = 43261596 # 00000010100101000001111010011100
    output_integer = 964176192 # 00111001011110000010100101000000
    assert main.reverse_bits(input_integer) == output_integer

def test_reverse_bits_example_2():
    input_integer = 4294967293 # 00000010100101000001111010011100
    output_integer = 3221225471 # 00111001011110000010100101000000
    assert main.reverse_bits(input_integer) == output_integer