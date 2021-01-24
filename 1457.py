# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        res = 0
        s = set()
        def func(root, path):
            nonlocal res
            if root:
                if not root.left and not root.right:
                    path ^= (1 << root.val)
                    count = 0
                    while path:
                        count += 1
                        path &= (path - 1)
                    if count <= 1:  res += 1
                else:
                    func(root.left, path ^ (1 << root.val))
                    func(root.right, path ^ (1 << root.val))
        func(root, 0)
        return res
            
                    