from typing import Optional


def hello():
    return ("Hello")

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        elements = []
        while(head):
            elements.append(head)
            head = head.next
        number_of_elements = len(elements)
        for i in range(number_of_elements):
            if i == number_of_elements // 2:
                elements[i].next = None
                break
            elements[number_of_elements -1 - i].next = elements[i + 1]
            elements[i].next = elements[number_of_elements -1 - i]
    
if __name__ == "__main__":
    sol = Solution()
    l2 = ListNode(7,None)
    l1 = ListNode(6,l2)
    l0 = ListNode(5,l1)
    sol.reorderList(l0)