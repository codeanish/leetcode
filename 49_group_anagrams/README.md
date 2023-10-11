# 49. Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.  

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.  

## Examples

### Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]  
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]  

### Example 2:

Input: strs = [""]  
Output: [[""]]  

### Example 3:

Input: strs = ["a"]  
Output: [["a"]]  
 
## Constraints:

1 <= strs.length <= 10^4  
0 <= strs[i].length <= 100  
strs[i] consists of lowercase English letters.  

## Notes

I kind of want to hash the strings so that we're creating a function that uniquely identifies a set of characters regardless of order so that f(abc) == f(bca).

If we have a function that takes the value of each character and somehow combines them without allowing for abe = bcd.

a = 1
b = 2
c = 3
d = 4
e = 5
f = 6

(1 + 2 + 3) = 6
(1 + 1 + 4) = 6

1*2*3 + 1+2+3= 12
1*1*6 + 1+1+6 = 14

all numbers added together + all numbers multiplied togther