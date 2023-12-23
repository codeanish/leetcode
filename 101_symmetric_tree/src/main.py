from typing import Optional


def hello():
    return ("Hello")

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSymmetric(self, root: Optional[TreeNode]):
        if not root:
            return True
        return self.isSame(root.left, root.right)

    def isSame(self, leftroot: Optional[TreeNode], rightroot: Optional[TreeNode]):
        if leftroot == None and rightroot == None:
            return True
        if leftroot == None or rightroot == None:
            return False
        if leftroot.val != rightroot.val:
            return False
        return self.isSame(leftroot.left, rightroot.right) and self.isSame(leftroot.right, rightroot.left)
    


if __name__ == "__main__":
    sol = Solution()
    n6 = TreeNode(3, None, None)
    n5 = TreeNode(4, None, None)
    n4 = TreeNode(4, None, None)
    n3 = TreeNode(3, None, None)
    n2 = TreeNode(2, n6, n5)
    n1 = TreeNode(2, n4, n3)
    n0 = TreeNode(1, n2, n1)
    print(sol.isSymmetric(n0))