from src import main

def test_hello():
    assert main.hello() == "Hello"

def test_length_of_last_word():
    sol = main.Solution()
    sol.lengthOfLastWord("Hello World") == 5
    sol.lengthOfLastWord("   fly me   to   the moon  ") == 4
    sol.lengthOfLastWord("luffy is still joyboy") == 6