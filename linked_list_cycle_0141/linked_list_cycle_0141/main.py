from typing import Optional


def hello():
    return ("Hello")

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    existing_pointers = set()
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        while head:
            if head in self.existing_pointers:
                return True
            else:
                self.existing_pointers.add(head)
            head = head.next
        return False
    
    def has_cycle_floyds_cycle_finding_algo(self, head: Optional[ListNode]) -> bool:
        slow_pointer = head
        fast_pointer = head
        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            if slow_pointer == fast_pointer:
                return True
        return False