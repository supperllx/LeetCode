# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        arr = []
        def func(root):
            if root:
                nonlocal arr
                if root.left:   func(root.left)
                arr.append(root)
                if root.right:  func(root.right)
        func(root)
        stack = []
        for i in range(len(arr) - 1):
            if arr[i].val > arr[i + 1].val:
                stack.append((arr[i], arr[i + 1]))
        if len(stack) == 1: stack[0][0].val, stack[0][1].val = stack[0][1].val, stack[0][0].val
        else: stack[0][0].val, stack[1][1].val = stack[1][1].val, stack[0][0].val
        
        