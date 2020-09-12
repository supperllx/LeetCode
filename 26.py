class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <=1:
            return len(nums)
        p1 = 0
        p2 = 1
        while p2 < len(nums):
            if nums[p1] == nums[p2]:
                p2+=1
            else:
                p1+=1
                nums[p1] = nums[p2]
                p2+=1
        return p1+1
        