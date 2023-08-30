# 191. Number of 1 bits

Write a function that takes the binary representation of an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

**Note**:

Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type. It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3, the input represents the signed integer. -3.
 
## Examples

### Example 1:

Input: n = `00000000000000000000000000001011`  
Output: 3  
Explanation: The input binary string `00000000000000000000000000001011` has a total of three '1' bits.

### Example 2:

Input: n = `00000000000000000000000010000000`  
Output: 1  
Explanation: The input binary string `00000000000000000000000010000000` has a total of one '1' bit.

### Example 3:

Input: n = `11111111111111111111111111111101`  
Output: 31  
Explanation: The input binary string `11111111111111111111111111111101` has a total of thirty one '1' bits.
 

### Constraints:

The input must be a binary string of length 32.
 
Follow up: If this function is called many times, how would you optimize it?

## Notes:

One could initially think that the simple solution here is to get a binary string and then count the instances of 1 in the string. This is my first implementation The implementation hamming_weight_crude_method does exactly this. The complexity of the solution I have is O(1) as the operation is on a 32bit integer, so it will always take 32 iterations in the loop - albeit the bit(n) string is often a short string given a small number.

Rather than using binary strings and equality operations, the next approach would be to use bitwise operations, one bit at a time through the value. This time we'll check if the last bit is 1 before shifting the bits one to the right in a loop. The implmentation hamming_weight_bitwise_method does this. The complexity of the solution is again O(1) as this takes 32 iterations to deal with a 32 bit integer. The benefit of this solution versus the string based solution is that it's likely to be faster and also use less memory.

Making the hamming_weight_bitwise_method more optimised requires you to reduce the number of loops by only iterating the number of times that there are 1's in the binary representation of the integer. The trick here is to logic AND n and n-1 together in the loop every time a 1 is encountered. This has the effect of looking at the last 1 in the binary representation of n and subtracting 1 from it. Then when you AND it together, everything to the left of that bit is left intact, while everything to the right is discarded. The result is incremented for each loop.

One interesting thing I learnt is that when checking if something is > 0, it's much more time efficient to just check like this:

```
if w:
    [code here]

```
versus

```
if w > 0:
    [code here]

```

The follow up question asked what we could consider if we were going to run this function a lot of times. I tested out a caching solution, whereby we pre cache each hamming weight for every 32 bit integer. This isn't particularly feasible as it would take around 25 minutes (on my computer) to cache all the hamming weights for each of the 32 bit integers. Moreover, this requires a lot, and I mean a lot of memory. For reference, without any caching, the memory footprint of the python process is ~12 MB. If we cache just all 24 bit integers, it consumes around 1.4 GB. The number of 32 bit integers is 256x more than the number of 24 bit integers, so we could summise we'd need 358 GB of memory to store that many hamming weights. Clearly not very practical on my macbook.