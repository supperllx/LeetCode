# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        elif len(nums) == 1:
            return TreeNode(nums[0])
        else:
            root = TreeNode(max(nums))
            i = nums.index(root.val)
            root.left = self.constructMaximumBinaryTree(nums[:i])
            root.right = self.constructMaximumBinaryTree(nums[i+1:])
            return root
        