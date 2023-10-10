from src import main

def test_hello():
    assert main.hello() == "Hello"

def test_character_replacement():
    sol = main.Solution()
    assert sol.characterReplacement("A",0) == 1
    assert sol.characterReplacement("B",1) == 1
    assert sol.characterReplacement("ABC",0) == 1
    assert sol.characterReplacement("ABA",0) == 1
    assert sol.characterReplacement("ABC",1) == 2
    assert sol.characterReplacement("ABA",1) == 3
    assert sol.characterReplacement("ABC",2) == 3
    assert sol.characterReplacement("AABABBA",1) == 4
    assert sol.characterReplacement("ABAB",2) == 4