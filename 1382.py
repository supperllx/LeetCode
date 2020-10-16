# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        array = []
        def func(root):
            if root:
                nonlocal array
                func(root.left)
                array.append(root)
                func(root.right)
        
        def build(x):
            if len(x) == 0: return None
            else:
                mid = len(x) // 2
                root = x[mid]
                root.left = build(x[:mid])
                root.right = build(x[mid+1:])
                return root
        func(root)
        return build(array)
