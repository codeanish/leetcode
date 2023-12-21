import sys
from typing import Optional


def hello():
    return ("Hello")

class TreeNode:
    def __init__(self, val: int=0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None) -> None:
        self.val = val
        self.left = left
        self.right = right
    

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        INF = sys.maxsize
        
        def helper(node: Optional[TreeNode], lower: int, upper: int) -> bool:
            if not node:
                return True
            
            if lower < node.val < upper:
                return helper(node.left, lower, node.val) and helper(node.right, node.val, upper)
            
            else:
                return False

        return helper( node=root, lower=-INF, upper=INF )


if __name__ == "__main__":
    n4 = TreeNode(7, None, None)
    n3 = TreeNode(3, None, None)
    n2 = TreeNode(6, n3, n4)
    n1 = TreeNode(4, None, None)
    n0 = TreeNode(5, n1, n2)
    sol = Solution()
    print(sol.isValidBST(n0))