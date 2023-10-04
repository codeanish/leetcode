# 141. Linked List Cycle

Given head, the head of a linked list, determine if the linked list has a cycle in it.  

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.  

Return true if there is a cycle in the linked list. Otherwise, return false.  

## Examples

### Example 1:

Input: head = [3,2,0,-4], pos = 1  
Output: true  
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).  

### Example 2:

Input: head = [1,2], pos = 0  
Output: true  
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.  

### Example 3:

Input: head = [1], pos = -1  
Output: false  
Explanation: There is no cycle in the linked list.  
 

## Constraints:

The number of the nodes in the list is in the range [0, 104].  
-105 <= Node.val <= 105  
pos is -1 or a valid index in the linked-list.  
 

Follow up: Can you solve it using O(1) (i.e. constant) memory?  

## Notes

My initial thought on how to solve this problem was to go through the linked list iteratively and store pointers to all the elements I encountered. This is not in O(1) space complexity, it's O(n). However it's still an O(n) time complexity solution. 

The algorithm that was used to eventually solve this with an O(1) space complexity was to use two pointers. The first moves at twice the speed of the first pointer. If the pointers eventually encounter the same element, then there is a cycle, but if not, there is no cycle. This also has the benefit of taking twice the steps in the algorithm on each cycle rather than stepping through once at a time. A description of why Floyds algorithm works is https://www.educative.io/answers/why-does-floyds-cycle-detection-algorithm-work.