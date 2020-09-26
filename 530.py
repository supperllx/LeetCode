# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        nums = []
        def func(root):
            if root:
                nonlocal nums
                func(root.left)
                nums.append(root.val)
                func(root.right)
        func(root)
        res = float('inf')
        for i in range(len(nums) - 1):
            if abs(nums[i+1] - nums[i]) < res:  res = abs(nums[i+1] - nums[i])
        return res