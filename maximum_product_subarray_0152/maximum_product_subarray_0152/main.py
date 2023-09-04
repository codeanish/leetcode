from typing import List


def hello():
    return ("Hello")

def maximum_product_subarray(input_array: List[int]) -> int:
    max_product = 0
    current_product = 0
    for element in input_array:
        if current_product == 0:
            current_product = element
        else:
            current_product *= element
        if current_product > max_product:
            max_product = current_product
    
    current_product = 0
    for i in range(len(input_array)-1, -1, -1):
        element = input_array[i]
        if current_product == 0:
            current_product = element
        else:
            current_product *= element
        if current_product > max_product:
            max_product = current_product
    return max_product

if __name__ == "__main__":
    print(maximum_product_subarray([2,3,-2,8]))