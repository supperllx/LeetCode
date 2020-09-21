# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        def func(root, s, path: List):
            if not root:
                return root
            else:
                if (not root.left) and (not root.right):
                    if root.val == s:
                        nonlocal res
                        path.append(root.val)
                        res.append(path)
                else:
                    path.append(root.val)
                    func(root.left, s - root.val, path.copy())
                    func(root.right, s - root.val, path.copy())
        func(root, sum, [])
        return res