# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:

        # @functools.lru_cache(None)
        def dfs(root):
            if root:
                l = dfs(root.left)
                r = dfs(root.right)
                select = root.val + r[1] + l[1]
                no_select = max(l) + max(r)
                return (select, no_select)
            else:   return (0, 0)
        
        return max(dfs(root))
