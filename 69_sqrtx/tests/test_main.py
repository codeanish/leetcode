from src import main

def test_hello():
    assert main.hello() == "Hello"

def test_sqrt():
    sol = main.Solution()
    assert sol.mySqrt(1) == 1
    assert sol.mySqrt(25) == 5
    assert sol.mySqrt(26) == 5
    assert sol.mySqrt(110) == 10
    assert sol.mySqrt(4) == 2