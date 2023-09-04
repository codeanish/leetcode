# 53. Maximum Subarray

Given an integer array nums, find the subarray (A subarray is a contiguous non-empty sequence of elements within an array) with the largest sum, and return its sum.

## Examples

### Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]  
Output: 6  
Explanation: The subarray [4,-1,2,1] has the largest sum 6.  

### Example 2:
Input: nums = [1]  
Output: 1  
Explanation: The subarray [1] has the largest sum 1.  

### Example 3:
Input: nums = [5,4,-1,7,8]  
Output: 23  
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.  

### Constraints:

* 1 <= nums.length <= 10^5
* -10^4 <= nums[i] <= 10^4
 

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

## Notes:

My first attempt at this is to code this up using a brute force approach. The brute force approach looks at all combinations of all contiguous numbers and is an O(n2) solution. There has to be a smarter approach here whereby we don't brute force it. In order to get an O(n) solution here, we can only check through the numbers one time for each value in the array.

[a,b,c,d]
[a,b,c] = [a] + [b] + [c]
[a,b,c] = [a,b] + [c]

All negative numbers are a bad thing in this, the only way we want to include them in our subarray is if contiguous numbers before/after those numbers positively contribute to a sum. Looking at the below array:

[-2,1,-3,4,-1,2,1,-5,4]

Ignore all combinations starting with i = 0 as it is negative and there is nothing to the left of it that has value
Start sum from i = 1, sum = 1 - MAX_SUM = 1
Check next value i = 2 sum = -2 we should ignore the sum from this point as it's negative
next i = 3, sum = 4, MAX_SUM = 4
next i = 4, sum = 3
next i = 5, sum = 5 MAX_SUM = 5
next i = 6, sum = 6 MAX_SUM = 6
next i = 7, sum = 1
next i = 8, sum = 5

Going through the algorithm needed here helped me to figure out exactly how it should work. This algorithm works in O(n) time and the solution can be found in largest_subarray_sum.

I'm not sure what the divide and conquer approach is, so this will be good to look at, for now I'm moving on.