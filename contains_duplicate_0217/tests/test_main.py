from contains_duplicate_0217 import main

def test_contains_duplicate():
    assert main.contains_duplicate([1,2,3,1]) == True
    assert main.contains_duplicate([1,2,3,4]) == False
    assert main.contains_duplicate([1,1,1,3,3,4,3,2,4,2]) == True


def test_contains_duplicate_set():
    assert main.contains_duplicates_set([1,2,3,1]) == True
    assert main.contains_duplicates_set([1,2,3,4]) == False
    assert main.contains_duplicates_set([1,1,1,3,3,4,3,2,4,2]) == True