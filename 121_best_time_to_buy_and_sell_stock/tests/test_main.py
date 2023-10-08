from src import main

def test_max_profit():
    assert main.max_profit([7,1,5,3,6,4]) == 5
    assert main.max_profit([7,6,4,3,1]) == 0

def test_max_profit_optimised():
    assert main.max_profit_optimised([7,1,5,3,6,4]) == 5
    assert main.max_profit_optimised([7,6,4,3,1]) == 0