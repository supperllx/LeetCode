"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        else:
            temp = 0
            for child in root.children:
                temp = max(temp, self.maxDepth(child))
            return temp + 1