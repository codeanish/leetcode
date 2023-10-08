from typing import List


def hello():
    return ("Hello")

def running_sum_of_1d_array(nums: List[int]) -> List[int]:
    running_sum_array = [nums[0]]
    for i in range(1,len(nums)):
        running_sum_array.append(nums[i] + running_sum_array[i-1])
    return running_sum_array


if __name__ == "__main__":
    print(running_sum_of_1d_array([2,2,2,2]))