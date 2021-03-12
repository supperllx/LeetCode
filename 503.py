class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)
        stack = []
        for i in range(2 * len(nums) - 1):
            index = i % len(nums)
            while stack and nums[stack[-1]] < nums[index]:
                res[stack.pop()] = nums[index]
            stack.append(index)
        return res