from src import main

def test_hello():
    assert main.hello() == "Hello"

def test_add_two_numbers_same_length():
    sol = main.Solution()
    a2 = main.ListNode(6,None)
    a1 = main.ListNode(2,a2)
    a0 = main.ListNode(1,a1)
    b2 = main.ListNode(6,None)
    b1 = main.ListNode(2, b2)
    b0 = main.ListNode(1,b1)
    result = sol.addTwoNumbers(b0,a0)
    assert result.val == 2
    assert result.next.val == 4
    assert result.next.next.val == 2
    assert result.next.next.next.val == 1

def test_add_two_numbers_uneven_length():
    sol = main.Solution()
    a2 = main.ListNode(6,None)
    a1 = main.ListNode(2,a2)
    a0 = main.ListNode(1,a1)
    b3 = main.ListNode(1,None)
    b2 = main.ListNode(6,b3)
    b1 = main.ListNode(2, b2)
    b0 = main.ListNode(1,b1)
    result = sol.addTwoNumbers(b0,a0)
    assert result.val == 2
    assert result.next.val == 4
    assert result.next.next.val == 2
    assert result.next.next.next.val == 2

def test_add_two_numbers_example_2():
    sol = main.Solution()
    # l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    a7 = main.ListNode(9,None)
    a6 = main.ListNode(9,a7)
    a5 = main.ListNode(9,a6)
    a4 = main.ListNode(9,a5)
    a3 = main.ListNode(9,a4)
    a2 = main.ListNode(9,a3)
    a1 = main.ListNode(9,a2)
    b4 = main.ListNode(9,None)
    b3 = main.ListNode(9,b4)
    b2 = main.ListNode(9,b3)
    b1 = main.ListNode(9,b2)
    result = sol.addTwoNumbers(b1,a1)
    # [8,9,9,9,0,0,0,1]
    assert result.val == 8
    assert result.next.val == 9
    assert result.next.next.val == 9
    assert result.next.next.next.val == 9
    assert result.next.next.next.next.val == 0
    assert result.next.next.next.next.next.val == 0
    assert result.next.next.next.next.next.next.val == 0
    assert result.next.next.next.next.next.next.next.val == 1