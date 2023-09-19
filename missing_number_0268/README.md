# 268. Missing Number

Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

## Examples

### Example 1:

Input: nums = [3,0,1]  
Output: 2  
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.


### Example 2:

Input: nums = [0,1]  
Output: 2  
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.


### Example 3:

Input: nums = [9,6,4,2,3,5,7,0,1]  
Output: 8  
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
 

## Constraints:

* n == nums.length
* 1 <= n <= 10^4
* 0 <= nums[i] <= n
* All the numbers of nums are unique.
 

Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

## Notes:
There is a very straight forward solution to this problem utilising sets. I can find a complete set, then subtract the set I have from this set. The remaining element in the set is the missing number.

Rather than looking at each number to find unique numbers in the set, we can simply sum together all the numbers in the array and subtract this number from the sum of all integers below n.

This is not done in O(1) space complexity however so this is probably out.

For n = 3, the set of numbers should == 0,1,2,3
n = 1 sum of n numbers = 1
n = 2 sum of n numbers = 3
n = 3 sum of n numbers = 6
n = 4 sum of n numbers = 10
n = 5 sum of n numbers = 15

x               1
xx              2
xxx             3
xxxx            4
xxxxx           5
xxxxxx          6

The formula for the sum of all integers to n is

n * (n+1) // 2