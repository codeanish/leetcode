# 3. Longest Substring without repeating characters

Given a string s, find the length of the longest 
substring
 without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

## Notes

The most straight forward solution I can think of is to brute force this problem. For each starting character, check all the following values to see if we have a longer substring than previously.

The other alternative approach I came up with was to go right to left to see what the longest subset was. Perhaps I can go back from the longest subset and see if previous values can fall into this subset?