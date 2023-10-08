from src import main

def test_hello():
    assert main.hello() == "Hello"

def test_valid_parentheses():
    sol = main.Solution()
    assert sol.isValid("()") == True
    assert sol.isValid("()[]{}") == True
    assert sol.isValid("(") == False
    assert sol.isValid("([)]") == False