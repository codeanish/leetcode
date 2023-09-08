import math
from typing import List


def hello():
    return ("Hello")

def search_array_my_solution(nums: List[int], target: int) -> int:
    left_index = 0
    right_index = len(nums) - 1
    mid_index = 0

    while(left_index <= right_index):
        mid_index = math.floor((right_index+left_index)/2)
        # value increasing to the middle
        if nums[left_index] <= target < nums[mid_index]:
            # the search_value is in the left section
            right_index = mid_index -1
        # value increasing from mid to right
        elif nums[mid_index] < target <= nums[right_index]:
            # the search value is in the right section
            left_index = mid_index + 1
        # value decreasing from mid to right, but not caught before
        elif nums[mid_index] == target:
                return mid_index
        elif nums[mid_index] > nums[right_index]:
            if nums[mid_index] == target:
                return mid_index
            left_index = mid_index + 1
        # value decreasing left to mid, but not caught before
        elif nums[left_index] > nums[mid_index]:
            right_index = mid_index -1
        else:
            return -1

def search_array(nums:List[int], target:int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # Check if left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Otherwise, right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1