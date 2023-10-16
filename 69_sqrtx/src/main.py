def hello():
    return ("Hello")

class Solution:
    def mySqrt(self, x: int) -> int:
        root = 1
        while root * root <= x:
            root += 1
        return root -1