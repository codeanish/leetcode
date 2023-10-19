from typing import Optional


def hello():
    return ("Hello")

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root: 
            if root.left is None and root.right is None:
                return 1
            else:
                return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        return 0
    

if __name__ == "__main__":
    sol = Solution()
    t5 = TreeNode(7,None, None)
    t4 = TreeNode(15, None, None)
    t3 = TreeNode(9,None, None)
    t2 = TreeNode(20, t4, t5)
    t1 = TreeNode(3, t2, t3)
    print(sol.maxDepth(t1))