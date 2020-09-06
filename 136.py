class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        
        for j in d.keys():
            if d[j] == 1:
                return j

# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         res = 0
#         for i in nums:
#             res = res ^ i
#         return res
