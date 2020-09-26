# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        def func(root, d, l):
            if root:
                func(root.left, d, l)
                if root.val in d:   d[root.val] += 1
                else:   d[root.val] = 1
                l.append(root.val)
                func(root.right, d, l)
                return (d, l)
        d = {}
        l = []
        func(root, d, l)
        for i in l:
            if k == 2 * i and d[i] >= 2:
                return True
            elif (k - i) in d and k != 2 * i:
                return True
        return False