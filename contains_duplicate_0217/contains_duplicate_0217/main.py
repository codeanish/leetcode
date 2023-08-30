from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    existing_nums = {}
    for num in nums:
        if existing_nums.get(num):
            return True
        else:
            existing_nums[num] = True
    return False

def contains_duplicates_set(nums: List[int]) -> bool:
    existing_nums = set()
    for num in nums:
        if num in existing_nums:
            return True
        else:
            existing_nums.add(num)
    return False
        