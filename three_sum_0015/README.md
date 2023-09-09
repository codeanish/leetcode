# 15. 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

## Examples

### Example 1:

Input: nums = [-1,0,1,2,-1,-4]  
Output: [[-1,-1,2],[-1,0,1]]  

Explanation:  
* nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
* nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
* nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.

The distinct triplets are [-1,0,1] and [-1,-1,2].  
Notice that the order of the output and the order of the triplets does not matter.

### Example 2:

Input: nums = [0,1,1]  
Output: []  

Explanation: The only possible triplet does not sum up to 0.  

### Example 3:

Input: nums = [0,0,0]  
Output: [[0,0,0]]  

Explanation: The only possible triplet sums up to 0.
 

### Constraints:

3 <= nums.length <= 3000
-10^5 <= nums[i] <= 10^5

## Notes:

In order to find all triplets, a poor approach would be to perform an O(n^3) nested loop through the array. This is clearly not going to be a good solution.  

I think I came up with a rather horrible solution to this problem, but on inspection of some solutions on leetcode, there is indeed a relatively reasonable approach to solving this problem.

1. If there are >= 3 0's add [0,0,0] to the results
2. If there is at least 1 0, for each positive number, see if there is a corresponding negative number, if so add [-num, 0, num] to the results
3. For each combo (sum) of negative numbers, see if there is a positive number in existance, if so add a sorted [-a,-b,(a+b)]
4. For each combo (sum) of positive numbers, see if there is a negative number in existance, if so add a sorted [a,b,-(a+b)]
