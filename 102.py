# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def levelOrder(self, root: TreeNode) -> List[List[int]]:
#         d = {}
#         def func(root, level):
#             if root:
#                 nonlocal d
#                 if level in d:
#                     d[level].append(root.val)
#                 else:
#                     d[level] = [root.val]
#                 func(root.left, level + 1)
#                 func(root.right, level + 1)
#         func(root, 0)
#         return list(d.values())

# class Solution:
#     def levelOrder(self, root: TreeNode) -> List[List[int]]:
#         if not root:    return []
#         dq = collections.deque()
#         level = 0
#         dq.append((root, 0))
#         temp = []
#         res = []
#         while len(dq):
#             node = dq.popleft()
#             if node[1] > level:
#                 res.append(temp)
#                 temp = []
#                 temp.append(node[0].val)
#                 level += 1
#             else:
#                 temp.append(node[0].val)
#             if node[0].left:   dq.append((node[0].left, level + 1))
#             if node[0].right:  dq.append((node[0].right, level + 1))
#         res.append(temp)
#         return res

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:    return []
        dq = collections.deque()
        res = []
        dq.append(root)
        while len(dq):
            temp = []
            level_size = len(dq)
            for i in range(level_size):
                node = dq.popleft()
                temp.append(node.val)
                if node.left:   dq.append(node.left)
                if node.right:  dq.append(node.right)
            res.append(temp)
        return res