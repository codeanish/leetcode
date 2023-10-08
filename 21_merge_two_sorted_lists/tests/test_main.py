from src import main

def test_hello():
    assert main.hello() == "Hello"

def test_merge_two_lists_both_none():
    sol = main.Solution()
    list1 = None
    list2 = None
    result = sol.mergeTwoLists(list1, list2)
    assert result == None

def test_merge_two_lists_one_empty():
    sol = main.Solution()
    list1 = None
    list2 = main.ListNode(0)
    result = sol.mergeTwoLists(list1, list2)
    assert result == list2

    list3 = main.ListNode(0)
    list4 = None
    result = sol.mergeTwoLists(list3, list4)
    assert result == list3

def test_merge_two_lists():
    sol = main.Solution()
    e2 = main.ListNode(4)
    e1 = main.ListNode(2, e2)
    list1 = main.ListNode(1, e1)

    f2 = main.ListNode(4)
    f1 = main.ListNode(3, f2)
    list2 = main.ListNode(1, f1)

    result = sol.mergeTwoLists(list1, list2)
    assert result.val == 1
    next_element = result.next
    assert next_element.val == 1
    next_element = next_element.next
    assert next_element.val == 2
    next_element = next_element.next
    assert next_element.val == 3
    next_element = next_element.next
    assert next_element.val == 4
    next_element = next_element.next
    assert next_element.val == 4
    assert next_element.next is None