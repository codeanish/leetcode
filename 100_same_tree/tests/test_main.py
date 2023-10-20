from src import main

def test_hello():
    assert main.hello() == "Hello"

def test_same_tree_not_the_same():
    sol = main.Solution()
    t2 = main.TreeNode(2, None, None)
    t1 = main.TreeNode(1, t2, None)
    t3 = main.TreeNode(2, None, None)
    t4 = main.TreeNode(1, None, t3)
    assert sol.isSameTree(t1, t4) == False

def test_same_tree_true():
    sol = main.Solution()
    p3 = main.TreeNode(3, None, None)
    p2 = main.TreeNode(2, None, None)
    p1 = main.TreeNode(1, p2, p3)
    q3 = main.TreeNode(3, None, None)
    q2 = main.TreeNode(2, None, None)
    q1 = main.TreeNode(1, q2, q3)
    assert sol.isSameTree(p1, q1) == True

def test_same_tree_false():
    sol = main.Solution()
    p3 = main.TreeNode(1, None, None)
    p2 = main.TreeNode(2, None, None)
    p1 = main.TreeNode(1, p2, p3)
    q3 = main.TreeNode(2, None, None)
    q2 = main.TreeNode(1, None, None)
    q1 = main.TreeNode(1, q2, q3)
    assert sol.isSameTree(p1, q1) == False

def test_same_tree_three_deep_true():
    sol = main.Solution()
    p4 = main.TreeNode(4, None, None)
    p3 = main.TreeNode(3, p4, None)
    p2 = main.TreeNode(2, None, None)
    p1 = main.TreeNode(1, p2, p3)
    q4 = main.TreeNode(4, None, None)
    q3 = main.TreeNode(3, q4, None)
    q2 = main.TreeNode(2, None, None)
    q1 = main.TreeNode(1, q2, q3)
    assert sol.isSameTree(p1, q1) == True

def test_same_tree_three_deep_diff_val_false():
    sol = main.Solution()
    p4 = main.TreeNode(4, None, None)
    p3 = main.TreeNode(3, p4, None)
    p2 = main.TreeNode(2, None, None)
    p1 = main.TreeNode(1, p2, p3)
    q4 = main.TreeNode(8, None, None)
    q3 = main.TreeNode(3, q4, None)
    q2 = main.TreeNode(2, None, None)
    q1 = main.TreeNode(1, q2, q3)
    assert sol.isSameTree(p1, q1) == False

def test_same_tree_three_deep_false():
    sol = main.Solution()
    p4 = main.TreeNode(4, None, None)
    p3 = main.TreeNode(3, p4, None)
    p2 = main.TreeNode(2, None, None)
    p1 = main.TreeNode(1, p2, p3)
    q4 = main.TreeNode(4, None, None)
    q3 = main.TreeNode(3, None, q4)
    q2 = main.TreeNode(2, None, None)
    q1 = main.TreeNode(1, q2, q3)
    assert sol.isSameTree(p1, q1) == False

def test_same_tree_none_nodes():
    sol = main.Solution()
    assert sol.isSameTree(None, None) == True

def test_same_tree_one_none_node():
    sol = main.Solution()
    p1 = main.TreeNode(1)
    assert sol.isSameTree(p1, None) == False

def test_edge_case():
    sol = main.Solution()
    p5 = main.TreeNode(15, None, None)
    p2 = main.TreeNode(5, None, p5)
    p1 = main.TreeNode(10, p2, None)
    q3 = main.TreeNode(15, None, None)
    q2 = main.TreeNode(5, None, None)
    q1 = main.TreeNode(10, q2, q3)
    assert sol.isSameTree(p1, q1) == False 

# [10,5,null,null,15]
# [10,5,15]