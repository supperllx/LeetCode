# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def check(s, t):
            if (not s) and (not t): return True
            elif (not s) or (not t) or (s.val != t.val):  
                return False
            else:
                return check(s.left, t.left) and check(s.right, t.right)
        
        def func(s, t):
            if not s:   return False
            else:   return check(s, t) or func(s.left, t) or func(s.right, t)
        
        return func(s, t)