from typing import Optional


def hello():
    return ("Hello")


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        element_at_position = {}
        position = 0
        while head:
            element_at_position[position] = head
            position += 1
            head = head.next
        total_nodes = max(element_at_position.keys()) + 1
        if total_nodes - n > 0:
            element_at_position.get(total_nodes-n-1).next = element_at_position.get(total_nodes-n).next
        element_at_position.pop(total_nodes-n)
        if len(element_at_position) > 0:
            first_node = min(element_at_position.keys())
            return element_at_position.get(first_node)
        return None
    
    def remove_nth_from_end_two_pointers(self,head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = head
        j = head
        for _ in range(n):
            j = j.next
        if j == None: # Only happens when we're supposed to remove the first element
            return head.next
        while j.next != None:
            i = i.next
            j = j.next
        i.next = i.next.next
        return head

    def print_linked_list(self, head: Optional[ListNode]):
        current = head
        if current:
            while current.next:
                print(current.val)
                current = current.next
            print(current.val)


if __name__ == "__main__":
    sol = Solution()
    e1 = ListNode(1)
    e2 = ListNode(2)
    e3 = ListNode(3)
    e4 = ListNode(4)
    e5 = ListNode(5)
    e1.next = e2
    e2.next = e3
    e3.next = e4
    e4.next = e5
    sol.print_linked_list(e1)
    print("--------------------------------")
    sol.removeNthFromEnd(e1,2)
    sol.print_linked_list(e1)