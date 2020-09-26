# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# only if when every node has 0 or 2 children can we make sure of the structure
# class Solution:
#     def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
#         if len(pre) > 1:
#             root = TreeNode(pre[0])
#             L = post.index(pre[1]) + 1
#             root.left = self.constructFromPrePost(pre[1:1 + L], post[:L])
#             root.right = self.constructFromPrePost(pre[1 + L:], post[L:-1])
#             return root
#         elif len(pre) == 1: return TreeNode(pre[0])
#         else:   return None

class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if len(pre) > 0:
            root = TreeNode(pre[0])
            L = post.index(pre[1]) + 1 if len(pre) > 1 else 1
            root.left = self.constructFromPrePost(pre[1:L+1], post[:L])
            root.right = self.constructFromPrePost(pre[L+1:], post[L:-1])
            return root