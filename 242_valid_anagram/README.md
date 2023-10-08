# 242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## Examples

### Example 1:

Input: s = "anagram", t = "nagaram"  
Output: true  

### Example 2:

Input: s = "rat", t = "car"  
Output: false  
 

## Constraints:

1 <= s.length, t.length <= 5 * 104  
s and t consist of lowercase English letters.  
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

## Notes

My initial thought here was to create character arrays and sort the arrays in order to find if they are valid anagrams by ensuring that the two arrays were the same. This is slow as it requires sorting the arrays before comparing them.

Perhaps if I use a dictionary with the values, I can then compare the dictionaries for equality?

Unsurprisingly, this was insanely quick compared to the previous approach of creating arrays and comparing the arrays together. The code was also much more straight forward as I didn't have to sort the arrays. How much faster? 172x faster!