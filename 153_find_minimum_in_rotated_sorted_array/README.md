# 153. Find Minimum in Rotated Sorted Array

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

* [4,5,6,7,0,1,2] if it was rotated 4 times.
* [0,1,2,4,5,6,7] if it was rotated 7 times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.


### Example 1:

Input: nums = [3,4,5,1,2]  
Output: 1  
Explanation: The original array was [1,2,3,4,5] rotated 3 times.  

### Example 2:

Input: nums = [4,5,6,7,0,1,2]  
Output: 0  
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.  

### Example 3:

Input: nums = [11,13,15,17]  
Output: 11  
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
 

### Constraints:

* n == nums.length
* 1 <= n <= 5000
* -5000 <= nums[i] <= 5000
* All the integers of nums are unique.
* nums is sorted and rotated between 1 and n times.

## Notes

The O(n) solution is to simply loop through the values and stop when one value if less than the previous one and it's the minimum if going left to right. If that never happens, it's the first element. Lets code this up first.

How can we tell what the rotation level is? 
Rotation takes rightmost number and moves it to the left of the array
Take leftmost number, then look at middle number in array, if middle > left then rotation 

Looking at the array [0,1,2,4,5,6,7]
Length = 7
Look at midpoint 7/2 = 3.5 = 4th element (index = 3)
If 4th element > 1st element, then rotation is less than 1/2 * length

Ignore the left of the array, so now, find midpoint of remaining right hand side

Elements are unique... this means that there must be a certain amount of liberties you can take knowing that numbers don't repeat and just move a minimum of +1 between integers

Want to quickly find out how many 

If I go to the midpoint, and the number to the right of the midpoi

[3,4,5,1,2]
The midpoint is 5, we've already established that this has rotated more than once because:
3 is not smaller than 4 and 2 indicating it's not been rotated
3 is not bigger than 4 and 2 indicating that it's been rotated once

Given it's been rotated, If midpoint > first (5>3) then the remaining elements contain the minimum

This is now working. I'm looking forward to seeing what a good solution to this problem is as mine is far from elegant. My solution is found at find_minimum. I'm also unsure if this works for all test cases. Perhaps I'll create myself a random test harness to test it.