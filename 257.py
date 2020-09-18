# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []
        def func(root, path):
            if root:
                path += str(root.val)
                if (not root.left) and (not root.right):
                    nonlocal res
                    res.append(path)
                else:
                    path += '->'
                    func(root.left, path)
                    func(root.right, path)
        func(root, '')
        return res