# 1. Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

## Examples
### Example 1:
Input: nums = [2,7,11,15], target = 9

Output: [0,1]

Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

### Example 2:
Input: nums = [3,2,4], target = 6

Output: [1,2]

### Example 3:
Input: nums = [3,3], target = 6

Output: [0,1]
 

## Constraints:
* 2 <= nums.length <= 10^4
* -10^9 <= nums[i] <= 10^9
* -10^9 <= target <= 10^9
* Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

## Notes:

This is a problem that typically looks to you to traverse the array once to look at each value, then traverse the array again to find whether or not a solution exists. This is an O(n^2) solution to the problem. We can do better than this. 

In order to not loop through the array again for each value in the array, we need to use a more efficient data structure for lookups. A dictionary is a much better data structure for lookups as lookups are completed in O(1) time.

My solution was to create a dictionary for the array and then loop through the dictionary and see if that by subtracting the value I'm on from the target, see if there is a result in the dictionary. If there is a result, return the result. If not, continue to the next value in the dictionary.

My solution resulted in unnecesary compute as I could have just checked the dictionary at every step along the way if there was a solution already in it. While my complexity was also O(n), this was still not as optimised as the alternative solution I found.
