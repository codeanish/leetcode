def hello():
    return ("Hello")

import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub("[^a-zA-Z0-9]", "", s)
        s = s.lower()
        
        length_of_string = len(s)
        half_of_string = length_of_string//2
        
        for i in range(half_of_string):
            left = s[i]
            right = s[length_of_string - i - 1]
            if left != right:
                return False
        return True
    

if __name__ == "__main__":
    sol = Solution()
    first = sol.isPalindrome("I am a man:1")
    second = sol.isPalindrome("A man, a plan, a canal: Panama")
    print(first)
    print(second)

# If length = 8, need 4 iterations
# If length = 7, need 3 iterations