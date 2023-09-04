# 152. Maximum Product Subarray

Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

## Examples

### Example 1:

Input: nums = [2,3,-2,4]  
Output: 6  
Explanation: [2,3] has the largest product 6.  

### Example 2:

Input: nums = [-2,0,-1] 
Output: 0  
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 

### Constraints:

* 1 <= nums.length <= 2 * 10^4
* -10 <= nums[i] <= 10
* The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

## Notes

If we have a 0 in this array, we effectively split the array at this point, so we can have sub arrays before to the left and the right of the 0, but not including the 0.

2 3 -2 4
1. current product = 2 & max product = 2
2. current product = 6 & max product = 6
3. current product = -12
4. current product = -48

reverse
1. current product = 4
2. current product = -8
3. current product = -24
4. current product = -48

Unlike summing, you can't discard products here as every additional number has the chance to make the solution bigger, even from a position of a large negative product. Performing two passes one left to right and the other right to left are required. I'll build out some more test cases to see how much further this needs to go. Seems as though my solution works for the other test cases I've tried to write.