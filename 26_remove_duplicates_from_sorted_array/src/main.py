from typing import List


def hello():
    return ("Hello")

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_values = 0
        stored_value = -101 # 100 <= nums[i] <= nums so we can use one value below the minimum value
        for i in range(len(nums)):
            if nums[i] == stored_value:
                nums[i] = "_"
                continue
            nums[unique_values] = nums[i]
            unique_values += 1
            stored_value = nums[i]
        return unique_values