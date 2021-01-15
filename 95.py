# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        @functools.cache
        def func(start, end):
            if start > end:    return [None]
            else:
                temp_res = []
                for i in range(start, end + 1):
                    for l in func(start, i - 1):
                        for r in func(i+1, end):
                            root = TreeNode(val = i)
                            root.left = l
                            root.right = r
                            temp_res.append(root)
                return temp_res
        return func(1, n) if n > 0 else []
