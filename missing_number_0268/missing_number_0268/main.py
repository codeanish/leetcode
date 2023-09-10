from typing import List


def hello():
    return ("Hello")

def missing_number_set(nums: List[int]) -> int:
    total_set = set(range(len(nums) + 1))
    my_nums = set(nums)
    result = total_set - my_nums
    return result.pop()

if __name__ == "__main__":
    print(missing_number_set([0,1,2,4,5,6]))