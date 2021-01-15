class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p = 0
        for i, n in enumerate(nums):
            if n == 0:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1
        
        for i, n in enumerate(nums):
            if n == 1:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1