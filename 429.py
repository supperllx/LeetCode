"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        d = {}
        def func(root, level):
            if root:
                if level in d:  d[level].append(root.val)
                else:   d[level] = [root.val]
                for child in root.children:
                    func(child, level + 1)
        func(root, 0)
        return list(d.values())
                