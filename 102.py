# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        d = {}
        def func(root, level):
            if root:
                nonlocal d
                if level in d:
                    d[level].append(root.val)
                else:
                    d[level] = [root.val]
                func(root.left, level + 1)
                func(root.right, level + 1)
        
        func(root, 0)
        # res = []
        # i = 0
        # while i in d:
        #     res.append(d[i])
        #     i += 1
        
        return list(d.values())
        