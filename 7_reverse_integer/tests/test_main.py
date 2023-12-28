from src import main

def test_hello():
    assert main.hello() == "Hello"

def test_reverse():
    sol = main.Solution()
    assert sol.reverse(123) == 321
    assert sol.reverse(-123) == -321
    assert sol.reverse(120) == 21
    assert sol.reverse(1534236469) == 0