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
    visited: list[int] = list()
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        if root:
            if root.val not in self.visited:
                self.visited.append(root.val)
                self.inorderTraversal(root.left)
                self.inorderTraversal(root.right)
        
        return self.visited
    

if __name__ == "__main__":
    n2 = TreeNode(3, None, None)
    n1 = TreeNode(2, n2, None)
    n0 = TreeNode(1, None, n1)
    sol = Solution()
    print(sol.inorderTraversal(n0))
    # print(sol.inorderTraversal(None))
    # print(sol.inorderTraversal(TreeNode(1, None, None)))