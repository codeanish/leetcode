# 217. Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

## Examples 

### Example 1:

Input: nums = [1,2,3,1]  
Output: true

### Example 2:

Input: nums = [1,2,3,4]  
Output: false

### Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]  
Output: true
 
### Constraints:

* 1 <= nums.length <= 10^5
* -10^9 <= nums[i] <= 10^9

## Notes:

My initial thought was if you want to find duplicates in an array, you need to iterate through the array. If you encounter a number that you've encountered before, your function must return True otherwise if you iterate through the whole array with no duplicates, you return False. This means that you need a data structure which you can add numbers you've already encountered to and be able to quickly check if the next number exists in it already. My immediate thought was this is a dictionary as lookups from a dictionary are O(1) complexity. Couple that with the cost of iterating through the array O(n) and you have an overall algorithmic complexity of O(n).

My solution was contains_duplicate. I looked at some of the alternative solutions and found one I preferred to my own which was to use a set as opposed to a dictionary. A set is a built in class which allows for a much nicer syntax that a dictionary in this case as there is no symantic meaning to a value of the key. This solution is implemented as contains_duplicate_set. 