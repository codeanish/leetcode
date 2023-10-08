# 11. Container with the most water

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).  

Find two lines that together with the x-axis form a container, such that the container contains the most water.  

Return the maximum amount of water a container can store.  

Notice that you may not slant the container.  

## Examples

### Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]  
Output: 49  

Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.  

## Example 2:

Input: height = [1,1]  
Output: 1  
 

### Constraints:

n == height.length
2 <= n <= 10^5
0 <= height[i] <= 10^4

## Notes

The simple solution here which works straight away is to work out every area for every number, this is an O(n^2) solution and involved a nested loop. You can create some optimizations to skip sections of the array for when a minimum distance away is out of the bounds of the array. This however is still an O(n^2) solution.

An alternative approach is to assert that the area from the first to the last element in the array is x, in order to get an area bigger than this, the height of the elements needs to be higher than what came before. 

Start with calculating the area, then get the shortest side and bring it inward and repeat this procedure. This solves the solution in O(n). There are further optimizations here by essentially using the same logic within the loop to bring the sides in n times while the height of the element is still below the minimum height of the initial two heights.