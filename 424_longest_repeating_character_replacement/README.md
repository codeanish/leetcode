# 424. Longest Repeating Character Replacement

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

## Examples

### Example 1:

Input: s = "ABAB", k = 2  
Output: 4  
Explanation: Replace the two 'A's with two 'B's or vice versa.  

### Example 2:

Input: s = "AABABBA", k = 1  
Output: 4  
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".  
The substring "BBBB" has the longest repeating letters, which is 4.  
There may exists other ways to achive this answer too.  

### Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length

## Notes

I'm picturing a 2d array that has indices on one axes and the letters on the other axes as follows

| Letter | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A | T | T | F | T | F | F | T |
| B | F | F | T | F | T | T | F |

So the arrays 
A = [1,1,0,1,0,0,1]
B = [0,0,1,0,1,1,0]

Knowing k = 1, you can go through the arrays one by one and maintain the longest substring length
This solution would require you to step through every letter in the string from left to right
This would be an nxm problem space

This is a brute force solution to the problem and isn't the most optimal way to solve it. A better way to solve this kind of solution is using a sliding window style approach. Two pointers, a left pointer and a right pointer. Move the right pointer until you can no longer move it without violating the rules of the max number of replacements k, then move the left pointer. Do this till you get the right pointer to the end and get the maximum substring length in the solution.