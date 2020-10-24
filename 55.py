class Solution:
    def canJump(self, nums: List[int]) -> bool:
        res = 0
        for i, rightmost in enumerate(nums):
            if i <= res:
                res = max(res, i + rightmost)
            if res >= len(nums) -1: return True
        return False
