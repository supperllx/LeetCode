"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def func(root, res):
            if root:
                for child in root.children:
                    func(child, res)
                res.append(root.val)
                return res
        return func(root, [])