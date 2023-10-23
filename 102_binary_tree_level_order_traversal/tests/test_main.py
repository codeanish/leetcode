from src import main

def test_hello():
    assert main.hello() == "Hello"

def test_level_order_example():
    t5 = main.TreeNode(7, None, None)
    t4 = main.TreeNode(15, None, None)
    t3 = main.TreeNode(20, t4, t5)
    t2 = main.TreeNode(9, None, None)
    t1 = main.TreeNode(3, t2, t3)
    sol = main.Solution()
    result = sol.levelOrder(t1)
    assert len(result) == 3
    assert result[0][0] == 3
    assert result[1][0] == 9
    assert result[1][1] == 20
    assert result[2][0] == 15
    assert result[2][1] == 7

def test_level_order_2_levels():
    t3 = main.TreeNode(20, None, None)
    t2 = main.TreeNode(9, None, None)
    t1 = main.TreeNode(1, t2, t3)
    sol = main.Solution()
    result = sol.levelOrder(t1)
    assert len(result) == 2
    assert result[0][0] == 1
    assert result[1][0] == 9
    assert result[1][1] == 20

def test_level_order_single_node():
    t1 = main.TreeNode(1,None, None)
    sol = main.Solution()
    result = sol.levelOrder(t1)
    assert len(result) == 1
    assert result[0][0] == 1

def test_level_order_null_node():
    sol = main.Solution()
    result = sol.levelOrder(None)
    assert len(result) == 0