from typing import List


def hello():
    return ("Hello")

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if len(digits) == 0:
            return [1]
        last_value = digits[-1] + 1
        if last_value == 10:
            digits[-1] = 0
            digits[:-1] = self.plusOne(digits[:-1])
        else:
            digits[-1] = last_value
        return digits
    

if __name__ == "__main__":

    sol = Solution()
    print(sol.plusOne([]))