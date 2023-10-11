from src import main

def test_hello():
    assert main.hello() == "Hello"

def test_is_palindrome():
    sol = main.Solution()
    sol.isPalindrome(12) == False
    sol.isPalindrome(121) == True
    sol.isPalindrome(0) == True
    sol.isPalindrome(-121) == False
    sol.isPalindrome(111111111) == True