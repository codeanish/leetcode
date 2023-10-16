from src import main

def test_hello():
    assert main.hello() == "Hello"

def test_remove_duplicates():
    sol = main.Solution()
    assert sol.removeDuplicates([1,2,3]) == 3
    assert sol.removeDuplicates([1,1,2]) == 2
    assert sol.removeDuplicates([1,1,1,1,1,1,1,2,2,2,2,2]) == 2
    nums = [0,0,1,1,1,2,2,3,3,4]
    k = sol.removeDuplicates(nums)
    assert k == 5