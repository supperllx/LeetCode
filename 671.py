# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def findSecondMinimumValue(self, root: TreeNode) -> int:
#         def func(root):
#             if (root.left != None) and (root.right != None):
#                 if max(root.right.val, root.left.val) > root.val:
#                     return max(root.right.val, root.left.val)
#                 else:
#                     return min(func(root.left), func(root.right))
#             else:
#                 return -1
#         return func(root)

# class Solution:
#     def findSecondMinimumValue(self, root: TreeNode) -> int: #dfs
#         if not root:    return -1
#         res = float('inf')
#         min_val = root.val
#         def func(root):
#             if root and root.left and root.right:
#                 nonlocal res, min_val
#                 temp = max(root.left.val, root.right.val)
#                 if temp != min_val: res = min(res, temp)
#                 if root.left.val == min_val:    func(root.left)
#                 if root.right.val == min_val:   func(root.right)
#         func(root)
#         return res if res != float('inf') else -1

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int: #bfs
        if not root:    return -1
        dq = collections.deque()
        dq.append(root)
        min_val = root.val
        res = float('inf')
        while len(dq):
            node = dq.popleft()
            if node.left:
                if node.left.val != min_val:
                    res = min(res, node.left.val)
                else:
                    dq.append(node.left)
            if node.right:
                if node.right.val != min_val:
                    res = min(res, node.right.val)
                else:
                    dq.append(node.right)
        return res if res != float('inf') else -1