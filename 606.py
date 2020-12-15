# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if t:
            if not t.left and not t.right:
                return str(t.val)
            else:
                s = str(t.val)
                s = s + '(' + self.tree2str(t.left) + ')'
                if t.right:  s = s + '(' + self.tree2str(t.right) + ')'
                return s
        else: return ''
        
        