# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        d = {}
        res = 0
        def func(root, pos, level):
            if root:
                nonlocal d, res
                if level in d:
                    d[level][0] = min(d[level][0], pos)
                    d[level][1] = max(d[level][1], pos)
                else:
                    d[level] = [pos, pos]
                if res < d[level][1] - d[level][0] + 1: res = d[level][1] - d[level][0] + 1
                func(root.left, pos * 2, level + 1)
                func(root.right, pos * 2 + 1, level + 1)
        func(root, 0, 0)
        # res = 0
        # for i in d.values():
        #     res = i[1] - i[0] + 1 if res < i[1] - i[0] + 1 else res
        return res