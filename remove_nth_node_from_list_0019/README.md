# 19. Remove Nth Node from End of List

Given the head of a linked list, remove the nth node from the end of the list and return its head.  

## Examples

### Example 1:

Input: head = [1,2,3,4,5], n = 2  
Output: [1,2,3,5]  

### Example 2:

Input: head = [1], n = 1  
Output: []  

### Example 3:

Input: head = [1,2], n = 1  
Output: [1]  
 
## Constraints:

The number of nodes in the list is sz.  
1 <= sz <= 30  
0 <= Node.val <= 100  
1 <= n <= sz  
 

Follow up: Could you do this in one pass?

## Notes

My initial thought is that we start traversing the linked list until we hit the nth element. We should get the next value from the nth element and set the next value on the n-1th element to the next value of n.

Oops, my mistake, it's actually after the nth element from the end, not from the beginning. Perhaps now I should keep a dictionary of elements where the key is the element position and the value is a pointer to the node.

I must love a good dictionary, it seems like the better accepted solutions always seem to be using a couple of pointers in these sort of traversal things. The idea was take two pointers (i and j), move j to the point at which it's n elements away from i. Then increment both pointers together until j reaches the end, at which point, i is the element that needs to be removed.