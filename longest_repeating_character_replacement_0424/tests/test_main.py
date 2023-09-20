from longest_repeating_character_replacement_0424 import main

def test_hello():
    assert main.hello() == "Hello"


def test_character_replacement():
    assert main.character_replacement('', 0) == 0
    assert main.character_replacement('ABAB', 2) == 4
    assert main.character_replacement('AABABBA', 1) == 4
    assert main.character_replacement('AAAB', 0) == 3
    assert main.character_replacement('ABBB', 2) == 4