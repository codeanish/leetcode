from remove_nth_node_from_list_0019 import main

def test_hello():
    assert main.hello() == "Hello"

def test_example_1():
    sol = main.Solution()
    e1 = main.ListNode(1)
    e2 = main.ListNode(2)
    e3 = main.ListNode(3)
    e4 = main.ListNode(4)
    e5 = main.ListNode(5)
    e1.next = e2
    e2.next = e3
    e3.next = e4
    e4.next = e5
    head = sol.remove_nth_from_end_two_pointers(e1,2)
    assert e1.next == e2
    assert e2.next == e3
    assert e3.next == e5
    assert e5.next is None
    assert head is e1

def test_example_2():
    sol = main.Solution()
    e1 = main.ListNode(1)
    head = sol.removeNthFromEnd(e1,1)
    assert head is None

def test_example_3():
    sol = main.Solution()
    e1 = main.ListNode(1)
    e2 = main.ListNode(2)
    e1.next = e2
    head = sol.removeNthFromEnd(e1, 1)
    assert head is e1
    assert head.next is None

def test_example_4():
    sol = main.Solution()
    e1 = main.ListNode(1)
    e2 = main.ListNode(2)
    e1.next = e2
    head = sol.removeNthFromEnd(e1,2)
    assert head is e2
    assert head.next is None