# class Solution:
#     def firstMissingPositive(self, nums: List[int]) -> int:
#         n = len(nums)
#         s = set()
#         for i, j in enumerate(nums):
#             if j > 0:   s.add(j)
#         res = 1
#         while res in s:
#             res += 1
#         return res

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i, j in enumerate(nums):
            if j <= 0:  nums[i] = n + 1
        
        for i, j in enumerate(nums):
            if 0 < (j := abs(j)) < n + 1:
                nums[j - 1] = -abs(nums[j - 1])
        
        for i in range(n):
            if nums[i] > 0: return i + 1
        return n + 1

