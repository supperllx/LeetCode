# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        d = {}
        def func(root):
            if root:
                nonlocal d
                if root.val in d:
                    d[root.val] += 1
                else:
                    d[root.val] = 1
                func(root.left)
                func(root.right)
        
        func(root)
        m = 0
        for i in d.keys():
            m = d[i] if d[i] > m else m
        res = []
        for i in list(d.keys()):
            if d[i] == m:
                res.append(i)
        return res