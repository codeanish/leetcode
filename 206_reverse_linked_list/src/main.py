from typing import Optional


class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def append_list_node(head: Optional[ListNode], new_node: ListNode) -> Optional[ListNode]:
    current = head
    if current:
        while current.next:
            current = current.next
        current.next = new_node
    else:
        head = new_node
    return head

def print_linked_list(head: Optional[ListNode]):
    current = head
    if current:
        while current.next:
            print(current.value)
            current = current.next
        print(current.value)

def push_node_to_beginning(head: Optional[ListNode], new_node: ListNode) -> Optional[ListNode]:
    new_node.next = head
    head = new_node
    return head

def reverse(head: Optional[ListNode]) -> Optional[ListNode]:
    new_head = None
    current = head
    while current:
        next_node = current.next
        current.next = new_head
        new_head = current
        current = next_node
    return new_head


def hello():
    return ("Hello")

if __name__ == "__main__":
    e2 = ListNode(2)
    e1 = ListNode(1, e2)
    head = ListNode(0, e1)
    head = append_list_node(head, ListNode(3))
    head = push_node_to_beginning(head, ListNode(-1))
    # print_linked_list(head)
    reversed_head = reverse(head)
    print_linked_list(reversed_head)
