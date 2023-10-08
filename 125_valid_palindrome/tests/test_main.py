from src import main

def test_hello():
    assert main.hello() == "Hello"

def test_valid_palindrome():
    sol = main.Solution()
    assert sol.isPalindrome("A man, a plan, a canal: Panama") == True
    assert sol.isPalindrome("race a car") == False
    assert sol.isPalindrome(" ") == True
    assert sol.isPalindrome("0P") == False