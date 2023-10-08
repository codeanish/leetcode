from typing import List


def hello():
    return ("Hello")

def three_sum(nums: List[int]) -> List[List[int]]:
    results = set()

    negative_numbers = []
    positive_numbers = []
    zeros = []

    for num in nums:
        if num < 0:
            negative_numbers.append(num)
        elif num == 0:
            zeros.append(zeros)
        else:
            positive_numbers.append(num)

    # if there are at least 3 zeros, add to results
    if len(zeros) >= 3:
        results.add((0,0,0))

    # create sets for fast lookups O(1)
    negative_numbers_set = set(negative_numbers)
    positive_numbers_set = set(positive_numbers)

    # if there is at least one zero, then if there is a negative equivalent of a positve number, add to set
    if len(zeros) > 0:
        for num in positive_numbers_set:
            if -num in negative_numbers_set:
                results.add((-num, 0, num))

    # for each pair of negative numbers, is there a corresponding positive number?
    for i in range(len(negative_numbers)):
        for j in range(i+1, len(negative_numbers)):
            positive_search_value = -(negative_numbers[i] + negative_numbers[j])
            if positive_search_value in positive_numbers_set:
                results.add(tuple(sorted([negative_numbers[i], negative_numbers[j], positive_search_value])))

    # for each pair of positive numbers, is there a corresponding negative number?
    for i in range(len(positive_numbers)):
        for j in range(i+1, len(positive_numbers)):
            negative_search_value = -(positive_numbers[i] + positive_numbers[j])
            if negative_search_value in negative_numbers_set:
                results.add(tuple(sorted([positive_numbers[i], positive_numbers[j], negative_search_value])))

    return [list(x) for x in results]
