from valid_anagram_0242 import main

def test_hello():
    assert main.hello() == "Hello"

def test_valid_anagram():
    sol = main.Solution()
    assert sol.isAnagram("abc", "def") == False
    assert sol.isAnagram("abc", "bc") == False
    assert sol.isAnagram("a", "b") == False
    assert sol.isAnagram("a", "aaa") == False
    assert sol.isAnagram("abc", "cba") == True
    # s = "anagram", t = "nagaram"
    assert sol.isAnagram("anagram", "nagaram") == True
    assert sol.isAnagram("rat", "car") == False