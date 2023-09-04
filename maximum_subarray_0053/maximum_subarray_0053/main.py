from typing import List


def hello():
    return ("Hello")

def largest_subarray_sum_n2(input_array: List[int]) -> int:
    if len(input_array) == 1:
        return input_array[0]
    max_sum = input_array[0]
    # What is python for enumerate when I just want an index? It makes sense to create just an index array for this
    for beginning_index, value in enumerate(input_array):
        for end_index, end_value in enumerate(input_array):
            if end_index < beginning_index:
                continue
            if sum(input_array[beginning_index:end_index+1:]) > max_sum:
                max_sum = sum(input_array[beginning_index:end_index+1:])
    return max_sum

def largest_subarray_sum(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    max_sum = nums[0]
    current_sum = nums[0]
    is_first = True
    for element in nums:
        if is_first == True:
            is_first = False
            continue
        current_sum = current_sum + element
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < element:
            current_sum = element
            if element > max_sum:
                max_sum = element
    return max_sum


if __name__ == "__main__":
    print(largest_subarray_sum([1,-1,1,1,-5,1])) # Should == 2
