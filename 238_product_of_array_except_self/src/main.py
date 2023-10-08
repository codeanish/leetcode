from typing import List
import math

def hello():
    return ("Hello")


def product_except_self_n2(nums: List[int]) -> List[int]:
    length = len(nums)
    return_array = [1] * length
    for i in range(length):
        # Slice the array to the left and the right of the element we're at.
        return_array[i] = math.prod(nums[0:i]) * math.prod(nums[i+1:])
    return return_array

def product_except_self(nums: List[int]) -> List[int]:
    length = len(nums)
    return_array = [1] * length
    left_product = 1
    for i in range(length):
        left_product *= nums[i-1] if i >= 1 else 1
        return_array[i] = left_product
    right_product = 1
    for i in range(length)[::-1]:
        right_product *= nums[i+1] if i < length - 1 else 1
        return_array[i] *= right_product
    return return_array


if __name__ == "__main__":
    print(product_except_self([1,2,3,4]))