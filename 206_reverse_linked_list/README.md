# 206. Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.

## Examples

### Example 1:

Input: head = [1,2,3,4,5]  
Output: [5,4,3,2,1]  

### Example 2:

Input: head = [1,2]  
Output: [2,1]  

## Example 3:

Input: head = []  
Output: []  

## Constraints:

The number of nodes in the list is the range [0, 5000].  
-5000 <= Node.val <= 5000

## Notes

Implementing a singly linked list means a having a node that links to the next node in the list. Appending a value to the list causes you to iterate through the list and then at the end add a new node by setting the next value on the last node to the new node. Putting a node at the beginning of a list means putting the next value to the previous head and returning the new head as the new node.

Reversing a singly linked list can be done by going through the linked list and each time you encounter a node, putting that node to the beginning of the list of nodes.