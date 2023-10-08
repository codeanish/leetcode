# 338. Counting bits

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

## Examples:

### Example 1:

Input: n = 2  
Output: [0,1,1]  

Explanation:
* 0 --> 0
* 1 --> 1
* 2 --> 10

### Example 2:

Input: n = 5  
Output: [0,1,1,2,1,2]  

Explanation:
* 0 --> 0
* 1 --> 1
* 2 --> 10
* 3 --> 11
* 4 --> 100
* 5 --> 101
 
## Constraints:

0 <= n <= 10^5
 

## Follow up:

* It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
* Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?

## Notes:
Again, it feels as though I've taken a rather convoluteed approach to solving what is an "easy" problem. I put in a whole bunch of bit value barriers, my theory being that if I want to find the number of 1 bits in the number 11, I can do it by initially subtracting a bit barrier (the nearest being 8) from 11, and with the leftovers = 5, lookup the number of 1 bits in 5 (which I've previously computed) and add 1 to it.

The simple solution does this way more succiently than how I've approached this by bit shifting the number 11 to the right by 1 bit, which essentially gives you 5 to look up a previously computed value and adding a modulus of 2 to the result, modulus of 2 is 0 if the value is even, or 1 if it's odd. I think doing some more bitwise operations and becoming more comfortable with them will enable me to solve these types of questions better.