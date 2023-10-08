# 20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

* Open brackets must be closed by the same type of brackets.
* Open brackets must be closed in the correct order.
* Every close bracket has a corresponding open bracket of the same type.
 
## Examples

### Example 1:

Input: s = "()"  
Output: true  

### Example 2:

Input: s = "()[]{}"  
Output: true  

### Example 3:

Input: s = "(]"  
Output: false  
 

## Constraints:

1 <= s.length <= 104  
s consists of parentheses only '()[]{}'.

## Notes

My initial thought was to count open brackets, then subtract closed bracket, if at the end, the sum of each type of bracket is 0, then it's valid. This is however broken by the rule that states brackets must be closed in the correct order. So the following string is invalid

"([)]"

So perhaps creating a stack of brackets last in first out and ensuring that if I add a closing bracket, the element removed from the stack must be of the same type as the previous one.

One thing I'm noticing in common is that I'm not designing enough possible test cases myself. I should do this to ensure I capture all the edge cases I can think of.