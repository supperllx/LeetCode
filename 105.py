# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(inorder):
            root = TreeNode(preorder[0])
            # for i in range(len(inorder)):
            #     if inorder[i] == root.val:
            #         break
            i = inorder.index(root.val)
            root.left = self.buildTree(preorder[1:i+1], inorder[0:i])
            root.right = self.buildTree(preorder[i+1:], inorder[i+1:])
            return root