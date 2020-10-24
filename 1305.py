# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def func(root, l):
            if root:
                func(root.left, l)
                l.append(root.val)
                func(root.right, l)
        
        l1 = []
        l2 = []
        func(root1, l1)
        func(root2, l2)
        res = []
        p1 = p2 = 0
        while p1 < len(l1) and p2 < len(l2):
            if l1[p1] < l2[p2]:
                res.append(l1[p1])
                p1 += 1
            else:
                res.append(l2[p2])
                p2 += 1
        res += l1[p1: ] if p1 < len(l1) else l2[p2: ]
        return res
        