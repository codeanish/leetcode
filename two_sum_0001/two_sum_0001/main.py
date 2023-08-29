from typing import List

def find_two_sum_in_array(nums: List[int], target: int) -> List[int]:
    for i, value in enumerate(nums):
        for j, next_value in enumerate(nums):
            if i == j:
                continue
            if value + next_value == target:
                return [i, j]

# Using a dictionary doesn't work because there are keys that are not unique when transposing an array into a dictionary
# Instead for an array like [3,5,3,2,6], create a dictionary like {2:[3], 3:[0,3], 5:[2], 6:[4]}
def find_two_sum_in_array_optimised(nums: List[int], target: int) -> List[int]:
    dict_of_nums = {}
    for i, value in enumerate(nums):
        if dict_of_nums.get(value) is not None:
            dict_of_nums[value].append(i)
        else:
            dict_of_nums[value] = [i]
    for value in dict_of_nums:
        target_reciprocal = target - value
        if target_reciprocal == value and len(dict_of_nums[value]) == 2:
            return dict_of_nums[value]

        solution = dict_of_nums.get(target_reciprocal)
        if solution is not None and dict_of_nums.get(value)[0] is not dict_of_nums.get(target_reciprocal)[0]:
            return [dict_of_nums[value][0], dict_of_nums[target_reciprocal][0]]


# Unlike my solution, he didn't create a dictionary of all numbers and then have a list of indexes for the numbers
# Instead as he traverses the nums array, he looks up the seen dictionary if the recoprical is in there, if not, he adds it
# When he finds a reciprocal in the seen dictionary, the problem is solved
def find_two_sum_in_array_someone_elses_solution(nums: List[int], target: int) -> List[int]:
    seen = {}
    for i, value in enumerate(nums):
        remaining = target - nums[i]
        if remaining in seen:
            return [i, seen[remaining]]
        else:
            seen[value] = i