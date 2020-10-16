# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]: #DFS. wrong answer
        d = collections.defaultdict(list)
        start = float('inf')
        end = -float('inf')
        def func(root, x, y):
            if root:
                nonlocal d, start, end
                start = min(start, x)
                end = max(end, x)
                d[x].append((y, root.val))
                func(root.left, x - 1, y + 1)
                func(root.right, x + 1, y + 1)
        func(root, 0, 0)
        return [[j[1] for j in sorted(d[i])] for i in range(start, end + 1) if i in d]

# class Solution:
#     def verticalTraversal(self, root: TreeNode) -> List[List[int]]: 
#         d = collections.defaultdict(list)
#         start, end = 0, 0
#         dq = collections.deque()
#         dq.append((root, 0))
#         while len(dq):
#             size = len(dq)
#             for i in range(size):
#                 node, pos = dq.pop()
#                 d[pos].append(node.val)
#                 temp_l = node.left else None
#                 temp_r = node.right else None
#                 if temp_l and temp_r:
#                     dq += [temp_l, temp_r] if temp_l.val < temp_r.val else [temp_r, temp_l]
#                 elif temp_l or
