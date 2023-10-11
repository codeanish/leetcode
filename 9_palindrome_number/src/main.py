def hello():
    return ("Hello")

class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        length_of_string = len(str_x)
        for i in range(length_of_string//2):
            if str_x[i] != str_x[length_of_string-i-1]:
                return False
        return True
    
    def reverse_integer(self, x: int) -> int:
        reversed_int = 0
        while x != 0:
            digit = x % 10
            reversed_int = reversed_int * 10 + digit
            x //= 10
        return reversed_int