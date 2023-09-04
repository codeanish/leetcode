from random import randint
from typing import List
import math


def hello():
    return ("Hello")

def find_minimum(input_array: List[int]) -> int:
    length = len(input_array)
    if length == 1:
        return input_array[0]
    if length == 2:
        return min(input_array[0], input_array[1])
    
    first_value = input_array[0]
    next_value = input_array[1]
    last_value = input_array[length-1]
    # Unrotated array
    if first_value < next_value and first_value < last_value:
        return first_value
    # One rotation
    if first_value > next_value and first_value > last_value:
        return next_value
    
    midpoint = math.floor(length/2)
    mid_value = input_array[midpoint]
    if mid_value > first_value:
        # choose right hand side
        return find_minimum(input_array[midpoint+1:length:1])
    else:
        # chose left hand side
        return find_minimum(input_array[0:midpoint:1])
    

if __name__ == "__main__":
    count = 0
    print(find_minimum([3,4,5,1,2]))
    # array_of_arrays = []
    # for i in range(10):
    #     length_of_array = randint(1,10)
    #     my_array = []
    #     for j in range(length_of_array):
    #         my_array.append(randint(-5000,5000))
    #     array_of_arrays.append(my_array)
    # print(array_of_arrays)