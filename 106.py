# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(postorder):
            root = TreeNode(postorder[-1])
            # for i in range(len(inorder)):
            #     if inorder[i] == root.val:
            #         break
            i = inorder.index(root.val)
            root.left = self.buildTree(inorder[:i], postorder[:i])
            root.right = self.buildTree(inorder[i+1:], postorder[i:-1])
            return root