# 125. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

## Examples

### Example 1:

Input: s = "A man, a plan, a canal: Panama"  
Output: true  
Explanation: "amanaplanacanalpanama" is a palindrome.  

### Example 2:

Input: s = "race a car"  
Output: false  
Explanation: "raceacar" is not a palindrome.  

### Example 3:

Input: s = " "  
Output: true  
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.  
 

## Constraints:

1 <= s.length <= 2 * 105  
s consists only of printable ASCII characters.  

## Notes:

I decided the thing to do here was first to strip out any non-alphanumeric characters, then convert the whole string to lower. After this, we can just iterate through the elements using two pointers (left and right) and ensure that left == right. We can ignore the middle character in odd length strings as if left == right, then they are in fact palindromes.