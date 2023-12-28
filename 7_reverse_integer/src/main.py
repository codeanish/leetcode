def hello():
    return ("Hello")

class Solution:
    def reverse(self, x: int) -> int:
        is_negative = False
        if x < 0:
            is_negative = True
            x = abs(x)
        y = str(x)
        result = -int(y[::-1]) if is_negative else int(y[::-1])
        
        # -231 <= x <= 231 - 1
        if result <= -2**31 or result >= 2**31 -1:
            return 0
        return result