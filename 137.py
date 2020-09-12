# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         d = set()
#         for i in nums:
#             d.add(i)
#         return (3*sum(d) - sum(nums)) // 2

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