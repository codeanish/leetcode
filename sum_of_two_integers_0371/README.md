# 371. Sum of Two Integers

Given two integers a and b, return the sum of the two integers without using the operators + and -.

## Examples

### Example 1:

Input: a = 1, b = 2

Output: 3

### Example 2:

Input: a = 2, b = 3

Output: 5
 

## Constraints:

* -1000 <= a, b <= 1000

## Notes:

I've never tackled a problem like this, but it strikes me as though there must be a way of performing binary operations on the numbers in order to add them together.

This question requires some bitwise operations. The bitwise operators are:

* AND &
* OR |
* XOR ^
* NOT ~
* LEFT SHIFT <<
* RIGHT SHIFT >>

### AND &
0101  & 0100 = 0100

### OR |
0101 | 0010 = 0111

### XOR ^
0101 ^ 0110 = 0011

### NOT ~
~0101 = 1010

### LEFT SHIFT
0101 << 1 = 1010
0101 << 2 = 0100

### RIGHT SHIFT
0101 >> 1 = 0010
0101 >> 2 = 0001

We can use a combination fo bitwise operators & and ^ to perform addition through a recursive bitwise process. I can't pretend to properly understand why this works and didn't come up with the algorithm myself. This will require some further study.

> WTF is the mask? I kind of understood the bitwise operations before the mask got involved. I need to find out why this is what it is.
