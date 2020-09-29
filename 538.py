# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        # if root:
        #     v = root.val
        #     if root.left:   
        #         root.left.val = self.convertBST(root.left).val
        #         if root.left.val > v:   root.val += root.left.val
        #     if root.right:
        #         root.right.val = self.convertBST(root.right).val
        #         if root.right.val > v:  root.val += root.right.val
        #     return root
        r_sum = 0
        def func(root):
            if root:
                nonlocal r_sum
                func(root.right)
                root.val += r_sum
                r_sum = root.val
                func(root.left)
                return root
        return func(root)
            
