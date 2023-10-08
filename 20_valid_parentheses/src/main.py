def hello():
    return ("Hello")

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        stack = []
        closing_dict = {'}':'{', ')':'(', ']':'['}
        for char in s:
            if char in set(['(', '[', '{']):
                stack.append(char)
            elif char in set([')',']','}']) and len(stack) > 0:
                last_char = stack.pop()
                opening_for_char = closing_dict.get(char)
                if last_char != opening_for_char:
                    return False
            else:
                return False
        if len(stack) == 0:
            return True
        return False