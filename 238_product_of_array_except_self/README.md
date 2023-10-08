# 238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

## Examples

### Example 1:

Input: nums = [1,2,3,4]  
Output: [24,12,8,6]  

## Example 2:

Input: nums = [-1,1,0,-3,3]  
Output: [0,0,9,0,0]
 

## Constraints:

* 2 <= nums.length <= 105
* -30 <= nums[i] <= 30
* The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

## Notes:
A simple O(n) solution here would be to find the product of the entire array and divide the answer by the value of the number that is being iterated. However as we're not allowed to use the division operator here, this is not an option. 

My initial approach yields an n^2 solution. This loops through the array of numbers and multiplies all the other numbers in the array together. This is achieved in the product_except_self_n2 solution.

Having looked at a solution to this problem, my intuition about slicing the array left and right has some legs, but the approach used can get this down to O(n) time with no additional memory overhead. It involves iterating through the array twice, once to compute the left slices and once to compute the right slices. This solution is completed in product_except_self. I must say, even though I knew intuitively what to do here, the array indexes and manipulation weren't straight forward to me.