"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def func(root, res):
            if root:
                res.append(root.val)
                for child in root.children:
                    func(child, res)
                return res
        return func(root, [])