from typing import List


def hello():
    return ("Hello")

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Still far too many accesses of list - not efficient
        vals_to_remove = nums.count(val)
        while vals_to_remove > 0:
            nums.remove(val)
            vals_to_remove -= 1
        
        # Another option
        # while val in nums:
        #     nums.remove(val)
        return len(nums)

if __name__ == "__main__":
    sol = Solution()
    nums = [0,1,2,2,3,0,4,2]
    print(sol.removeElement(nums, 2))
    print(nums)