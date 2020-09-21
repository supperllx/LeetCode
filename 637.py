# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        s = {}
        c = {}
        def func(root, level):
            if root:
                nonlocal s
                nonlocal c
                if level in s:
                    s[level] += root.val
                    c[level] += 1
                else:
                    s[level] = root.val
                    c[level] = 1
                func(root.left, level+1)
                func(root.right, level+1)
        func(root, 0)
        res = []
        for i in s.keys():
            res.append(s[i]/c[i])
        return res

