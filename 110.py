# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        ans = True
        def get_depth(p_root):
            nonlocal ans
            if not p_root:
                return 0
            else:
                d_left = get_depth(p_root.left)
                d_right = get_depth(p_root.right)
                if abs(d_left - d_right) > 1:
                    ans = False
                return max(d_left, d_right) + 1
        
        get_depth(root)
        return ans

