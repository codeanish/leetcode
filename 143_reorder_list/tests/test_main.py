from src import main

def test_hello():
    assert main.hello() == "Hello"

def test_reorder_list_one_element():
    sol = main.Solution()
    l0 = main.ListNode(5,None)
    sol.reorderList(l0)
    assert l0.next == None
    assert l0.val == 5

def test_reorder_list_two_elements():
    sol = main.Solution()
    l1 = main.ListNode(6,None)
    l0 = main.ListNode(5, l1)
    sol.reorderList(l0)
    assert l0.next == l1
    assert l0.val == 5
    assert l1.next == None
    assert l1.val == 6

def test_reorder_list_three_elements():
    sol = main.Solution()
    l2 = main.ListNode(7,None)
    l1 = main.ListNode(6,l2)
    l0 = main.ListNode(5,l1)
    sol.reorderList(l0)
    assert l0.next == l2
    assert l1.next == None
    assert l2.next == l1
    assert l0.val == 5
    assert l1.val == 6
    assert l2.val == 7

def test_reorder_list_four_elements():
    sol = main.Solution()
    l3 = main.ListNode(8,None)
    l2 = main.ListNode(7,l3)
    l1 = main.ListNode(6,l2)
    l0 = main.ListNode(5,l1)
    sol.reorderList(l0)
    assert l0.next == l3
    assert l1.next == l2
    assert l2.next == None
    assert l3.next == l1

def test_reorder_list_five_elements():
    sol = main.Solution()
    l4 = main.ListNode(5,None)
    l3 = main.ListNode(4,l4)
    l2 = main.ListNode(3,l3)
    l1 = main.ListNode(2,l2)
    l0 = main.ListNode(1,l1)
    sol.reorderList(l0)
    assert l0.next == l4
    assert l1.next == l3
    assert l2.next == None
    assert l3.next == l2
    assert l4.next == l1