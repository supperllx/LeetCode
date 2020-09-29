# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if (not root) or (root.val == p.val) or (root.val == q.val):    return root
        else:
            left_res = self.lowestCommonAncestor(root.left, p, q)
            right_res = self.lowestCommonAncestor(root.right, p, q)
            if (left_res != None) and (right_res != None):  return root
            elif (left_res != None) and (not right_res):    return left_res
            elif (not left_res) and (right_res != None):    return right_res
            else:   return None