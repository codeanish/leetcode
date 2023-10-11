from src import main

def test_hello():
    assert main.hello() == "Hello"

def test_group_anagrams():
    sol = main.Solution()
    strs = ["eat","tea","tan","ate","nat","bat"]
    grouped_anagrams = sol.groupAnagrams(strs)
    assert len(grouped_anagrams) == 3

    strs = [""]
    grouped_anagrams = sol.groupAnagrams(strs)
    assert len(grouped_anagrams) == 1

    strs = ["a"]
    grouped_anagrams = sol.groupAnagrams(strs)
    assert grouped_anagrams == [["a"]]
    assert len(grouped_anagrams) == 1