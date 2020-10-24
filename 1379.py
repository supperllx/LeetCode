# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def func(root, array):
            if root:
                func(root.left, array)
                array.append(root)
                func(root.right, array)
        l1 = []
        l2 = []
        func(original, l1)
        func(cloned, l2)
        for i in range(len(l1)):
            if l1[i] == target: return l2[i]