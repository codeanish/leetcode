from src import main

def test_hello():
    assert main.hello() == "Hello"

def test_invert_binary_tree_none():
    sol = main.Solution()
    assert sol.invertTree(None) == None

def test_invert_binary_tree_one_level():
    sol = main.Solution()
    t7 = main.TreeNode(9,None, None)
    assert sol.invertTree(t7) == t7

def test_invert_binary_tree_two_levels():
    sol = main.Solution()
    t7 = main.TreeNode(9,None, None)
    t6 = main.TreeNode(6,None, None )
    t5 = main.TreeNode(7,t6, t7)
    inverted_t5 = sol.invertTree(t5)
    assert inverted_t5.left == t7
    assert inverted_t5.right == t6

def test_invert_binary_tree_three_levels():
    sol = main.Solution()
    t7 = main.TreeNode(9,None, None)
    t6 = main.TreeNode(6,None, None )
    t5 = main.TreeNode(7,t6, t7)
    t4 = main.TreeNode(3, None, None)
    t3 = main.TreeNode(1, None, None)
    t2 = main.TreeNode(2, t3, t4)
    t1 = main.TreeNode(4, t2, t5)
    assert t1.left == t2
    assert t1.right == t5
    assert t2.left == t3
    assert t2.right == t4
    assert t5.left == t6
    assert t5.right == t7
    inverted_t1 = sol.invertTree(t1)
    assert inverted_t1.left == t5
    assert inverted_t1.right == t2
    assert inverted_t1.left.left == t7
    assert inverted_t1.left.right == t6
    assert inverted_t1.right.left == t4
    assert inverted_t1.right.right == t3