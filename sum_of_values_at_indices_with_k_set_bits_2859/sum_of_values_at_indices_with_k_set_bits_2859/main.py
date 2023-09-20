from typing import List


def hello():
    return ("Hello")

def sum_of_values_at_indices_with_k_set_bits(nums: List[int],k: int) -> int:
    print(bin(len(nums)-1))
    return len(nums) -1

if __name__ == "__main__":
    nums = [4,3,2,1,0]
    k = 2
    print(sum_of_values_at_indices_with_k_set_bits(nums, k))