class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        nums[:n - k] = nums[:n - k][::-1]
        nums[n - k:] = nums[n - k:][::-1]
        nums.reverse()
