from src import main

def test_hello():
    assert main.hello() == "Hello"

def test_has_cycle_false():
    sol = main.Solution()
    e2 = main.ListNode(2)
    e1 = main.ListNode(1)
    head = main.ListNode(0)
    head.next = e1
    e1.next = e2
    assert sol.hasCycle(head) == False

def test_has_cycle_true():
    sol = main.Solution()
    e2 = main.ListNode(2)
    e1 = main.ListNode(1)
    head = main.ListNode(0)
    head.next = e1
    e1.next = e2
    e2.next = e1
    assert sol.hasCycle(head) == True

def test_has_cycle_example_1():
    sol = main.Solution()
    # 3,2,0,-4
    head = main.ListNode(3)
    e1 = main.ListNode(2)
    e2 = main.ListNode(0)
    e3 = main.ListNode(-4)
    head.next = e1
    e1.next = e2
    e2.next = e3
    e3.next = e1
    assert sol.hasCycle(head) == True

def test_has_cycle_example_2():
    sol = main.Solution()
    # 1,2
    head = main.ListNode(1)
    e1 = main.ListNode(2)
    head.next = e1
    e1.next = head
    assert sol.hasCycle(head) == True

def test_has_cycle_example_3():
    sol = main.Solution()
    head = main.ListNode(1)
    assert sol.hasCycle(head) == False

def test_has_cycle_empty_list():
    sol = main.Solution()
    assert sol.hasCycle(None) == False




def test_has_cycle_floyd_false():
    sol = main.Solution()
    e2 = main.ListNode(2)
    e1 = main.ListNode(1)
    head = main.ListNode(0)
    head.next = e1
    e1.next = e2
    assert sol.has_cycle_floyds_cycle_finding_algo(head) == False

def test_has_cycle_floyd_true():
    sol = main.Solution()
    e2 = main.ListNode(2)
    e1 = main.ListNode(1)
    head = main.ListNode(0)
    head.next = e1
    e1.next = e2
    e2.next = e1
    assert sol.has_cycle_floyds_cycle_finding_algo(head) == True

def test_has_cycle_floyd_example_1():
    sol = main.Solution()
    # 3,2,0,-4
    head = main.ListNode(3)
    e1 = main.ListNode(2)
    e2 = main.ListNode(0)
    e3 = main.ListNode(-4)
    head.next = e1
    e1.next = e2
    e2.next = e3
    e3.next = e1
    assert sol.has_cycle_floyds_cycle_finding_algo(head) == True

def test_has_cycle_floyd_example_2():
    sol = main.Solution()
    # 1,2
    head = main.ListNode(1)
    e1 = main.ListNode(2)
    head.next = e1
    e1.next = head
    assert sol.has_cycle_floyds_cycle_finding_algo(head) == True

def test_has_cycle_floyd_example_3():
    sol = main.Solution()
    head = main.ListNode(1)
    assert sol.has_cycle_floyds_cycle_finding_algo(head) == False

def test_has_cycle_empty_list():
    sol = main.Solution()
    assert sol.has_cycle_floyds_cycle_finding_algo(None) == False