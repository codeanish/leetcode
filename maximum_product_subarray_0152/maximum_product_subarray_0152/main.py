from typing import List


def hello():
    return ("Hello")

def maximum_product_subarray(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    max_product = 0
    current_product = 0
    for element in nums:
        if current_product == 0:
            current_product = element
        else:
            current_product *= element
        if current_product > max_product:
            max_product = current_product
    
    current_product = 0
    for i in range(len(nums)-1, -1, -1):
        element = nums[i]
        if current_product == 0:
            current_product = element
        else:
            current_product *= element
        if current_product > max_product:
            max_product = current_product
    return max_product

if __name__ == "__main__":
    print(maximum_product_subarray([2,3,-2,8]))