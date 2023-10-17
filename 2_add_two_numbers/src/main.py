from typing import Optional


def hello():
    return ("Hello")

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        elements = []
        while l1 or l2:
            digit_value = (0 if l1 is None else l1.val) + (0 if l2 is None else l2.val) + carry
            carry = digit_value // 10
            digit_value = digit_value % 10
            elements.append(ListNode(digit_value))
            l1 = None if l1 is None else l1.next
            l2 = None if l2 is None else l2.next
        if carry == 1:
            elements.append(ListNode(1))
        for i in range(len(elements)-1):
            elements[i].next = elements[i + 1]
        return elements[0]

if __name__ == "__main__":
    sol = Solution()
    a2 = ListNode(6,None)
    a1 = ListNode(2,a2)
    a0 = ListNode(1,a1)
    b3 = ListNode(1,None)
    b2 = ListNode(6,b3)
    b1 = ListNode(2, b2)
    b0 = ListNode(1,b1)
    sol.addTwoNumbers(a0,b0)