from src import main

def test_hello():
    assert main.hello() == "Hello"

def test_maximum_depth_of_binary_tree():
    sol = main.Solution()
    t5 = main.TreeNode(7,None, None)
    t4 = main.TreeNode(15, None, None)
    t3 = main.TreeNode(9,None, None)
    t2 = main.TreeNode(20, t4, t5)
    t1 = main.TreeNode(3, t2, t3)
    # assert sol.maxDepth(t5) == 1
    assert sol.maxDepth(None) == 0
    assert sol.maxDepth(t5) == 1
    assert sol.maxDepth(t2) == 2
    assert sol.maxDepth(t1) == 3

def test_maximum_depth_of_binary_tree_unbalanced():
    sol = main.Solution()
    t7 = main.TreeNode(2, None, None)
    t6 = main.TreeNode(1, None, t7)
    t5 = main.TreeNode(7,None, t6)
    t4 = main.TreeNode(15, None, None)
    t3 = main.TreeNode(9,None, None)
    t2 = main.TreeNode(20, t4, t5)
    t1 = main.TreeNode(3, t2, t3)
    assert sol.maxDepth(t1) == 5
