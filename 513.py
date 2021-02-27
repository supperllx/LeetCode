# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def findBottomLeftValue(self, root: TreeNode) -> int:
#         d = {}
#         max_level = 0
#         def func(root, level):
#             if root:
#                 nonlocal d, max_level
#                 if level in d:  d[level].append(root.val)
#                 else:   d[level] = [root.val]
#                 max_level = max(max_level, level)
#                 func(root.left, level + 1)
#                 func(root.right, level + 1)
#         func(root, 0)
#         return d[max_level][0]

# class Solution:
#     def findBottomLeftValue(self, root: TreeNode) -> int:
#         max_level = -1
#         res = 0
#         def func(root, level):
#             if root:
#                 nonlocal res, max_level
#                 if level > max_level:
#                     res = root.val
#                     max_level = level
#                 func(root.left, level + 1)
#                 func(root.right, level + 1)
#         func(root, 0)
#         return res

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        res = 0
        dq = collections.deque()
        dq.append(root)
        while dq:
            res = dq[0].val
            for _ in range(len(dq)):
                curNode = dq.popleft()
                if curNode.left:
                    dq.append(curNode.left)
                if curNode.right:
                    dq.append(curNode.right)
        return res