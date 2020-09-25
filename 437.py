# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        res = 0
        def check_node(root, s):
            if root:
                if root.val == s:
                    nonlocal res
                    res += 1
                check_node(root.left, s - root.val)
                check_node(root.right, s - root.val)
        
        def check_tree(root, s):
            if root:
                check_node(root, s)
                check_tree(root.left, s)
                check_tree(root.right, s)
        
        check_tree(root, sum)
        return res
        