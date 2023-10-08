from typing import Optional


def hello():
    return ("Hello")

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # get heads
        if list1 is None and list2 is None:
            return None
        if list1 and list2 is None:
            return list1
        if list2 and list1 is None:
            return list2

        current = None
        head = None
        if list1.val <= list2.val:
            head = list1
            list1 = list1.next
            current = head
        else:
            head = list2
            list2 = list2.next
            current = head
        
        while list1 or list2:
            if list1 is None:
                current.next = list2
                current = list2
                list2 = list2.next
                continue
            if list2 is None:
                current.next = list1
                current = list1
                list1 = list1.next
                continue
            if list1.val <= list2.val:
                current.next = list1
                current = list1
                list1 = list1.next
            else:
                current.next = list2
                current = list2
                list2 = list2.next
        return head
    
def print_linked_list(head: Optional[ListNode]):
    current = head
    if current:
        while current.next:
            print(current.val)
            current = current.next
        print(current.val)

if __name__ == "__main__":
    sol = Solution()
    e2 = ListNode(4)
    e1 = ListNode(2, e2)
    list1 = ListNode(1, e1)

    f2 = ListNode(4)
    f1 = ListNode(3, f2)
    list2 = ListNode(1, f1)
    
    result = sol.mergeTwoLists(list1, list2)

    print_linked_list(result)