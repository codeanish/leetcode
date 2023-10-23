from typing import List, Optional


def hello():
    return ("Hello")

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        # Take first level and add the root value
        if root:
            result.append([root.val])
            
            level = []
            # Get the second level nodes
            if root.left:
                level.append(root.left)
            if root.right:
                level.append(root.right)
            
            # For each value in the nodes at this level, add them to the result
            while len(level) > 0:
                level_array = []
                new_level = []
                for node in level:
                    level_array.append(node.val)
                    if node.left:
                        new_level.append(node.left)
                    if node.right:
                        new_level.append(node.right)
                result.append(level_array)
                level = new_level
                
        return result