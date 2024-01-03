from typing import List


def hello():
    return ("Hello")

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [273.15 + celsius, celsius * 1.80 + 32]
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.convertTemperature(36.50))