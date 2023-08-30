from number_of_1_bits_0191 import main

def test_hamming_weight_crude_method():
    assert main.hamming_weight_crude_method(1) == 1
    assert main.hamming_weight_crude_method(2) == 1
    assert main.hamming_weight_crude_method(4) == 1
    assert main.hamming_weight_crude_method(8) == 1
    assert main.hamming_weight_crude_method(16) == 1
    assert main.hamming_weight_crude_method(3) == 2
    assert main.hamming_weight_crude_method(11) == 3
    assert main.hamming_weight_crude_method(int('11111111111111111111111111111101',2)) == 31


def test_hamming_weight_bitwise_method():
    assert main.hamming_weight_bitwise_method(1) == 1
    assert main.hamming_weight_bitwise_method(2) == 1
    assert main.hamming_weight_bitwise_method(4) == 1
    assert main.hamming_weight_bitwise_method(8) == 1
    assert main.hamming_weight_bitwise_method(16) == 1
    assert main.hamming_weight_bitwise_method(3) == 2
    assert main.hamming_weight_bitwise_method(11) == 3
    assert main.hamming_weight_bitwise_method(int('11111111111111111111111111111101',2)) == 31

def test_hamming_weight_bitwise_optimised():
    assert main.hamming_weight_bitwise_optimised(1) == 1
    assert main.hamming_weight_bitwise_optimised(2) == 1
    assert main.hamming_weight_bitwise_optimised(4) == 1
    assert main.hamming_weight_bitwise_optimised(8) == 1
    assert main.hamming_weight_bitwise_optimised(16) == 1
    assert main.hamming_weight_bitwise_optimised(3) == 2
    assert main.hamming_weight_bitwise_optimised(11) == 3
    assert main.hamming_weight_bitwise_optimised(int('11111111111111111111111111111101',2)) == 31