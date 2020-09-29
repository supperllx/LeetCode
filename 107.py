# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
#         d = {}
#         def func(root, level):
#             if root:
#                 if level in d:  d[level].append(root.val)
#                 else:   d[level] = [root.val]
#                 func(root.left, level + 1)
#                 func(root.right, level + 1)
#         func(root, 0)
#         return list(d.values())[::-1]

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:    return []
        dq = collections.deque()
        res = collections.deque()
        dq.append(root)
        while len(dq):
            temp = []
            level_size = len(dq)
            for i in range(level_size):
                cur_node = dq.popleft()
                temp.append(cur_node.val)
                if cur_node.left:   dq.append(cur_node.left)
                if cur_node.right:  dq.append(cur_node.right)
            res.appendleft(temp)
        return list(res)