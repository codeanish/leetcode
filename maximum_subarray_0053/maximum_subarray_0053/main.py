from typing import List


def hello():
    return ("Hello")

def largest_subarray_sum_n2(input_array: List[int]) -> int:
    max_sum = 0
    # What is python for enumerate when I just want an index? It makes sense to create just an index array for this
    for beginning_index, value in enumerate(input_array):
        for end_index, end_value in enumerate(input_array):
            if end_index < beginning_index:
                continue
            if sum(input_array[beginning_index:end_index+1:]) > max_sum:
                max_sum = sum(input_array[beginning_index:end_index+1:])
    return max_sum

def largest_subarray_sum(input_array: List[int]) -> int:
    max_sum = 0
    current_sum = 0
    for element in input_array:
        current_sum = current_sum + element
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < 0:
            current_sum = 0
    return max_sum


if __name__ == "__main__":
    print(largest_subarray_sum([1,-1,1,1,-5,1])) # Should == 2
