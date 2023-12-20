from typing import Optional


def hello():
    return ("Hello")

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        queue = []
        visited = []

        queue.append(root)
        visited.append(root)

        while queue:
            m = queue.pop()
            # print(m.val, end=" ")

            if m.left and m.left not in visited:
                queue.append(m.left)
                visited.append(m.left)
            
            if m.right and m.right not in visited:
                queue.append(m.right)
                visited.append(m.right)

        values = [k.val for k in visited]
        values.sort()
        return values[k-1]


if __name__ == "__main__":
    # n3 = TreeNode(2, None, None)
    # n2 = TreeNode(1, None, n3)
    # n1 = TreeNode(4, None, None)
    # n0 = TreeNode(3, n1, n2)

    # sol = Solution()
    # print(sol.kthSmallest(n0, 1))

    n5 = TreeNode(1, None, None)
    n4 = TreeNode(2, n5, None)
    n3 = TreeNode(4, None, None)
    n2 = TreeNode(3, n4, n3)
    n1 = TreeNode(6, None, None)
    n0 = TreeNode(5, n2, n1)

    sol = Solution()
    print(sol.kthSmallest(n0, 3))