# class Solution:
#     def maximumGap(self, nums: List[int]) -> int:
#         if len(nums) < 2:   return 0
#         nums.sort()
#         res = -float('inf')
#         for i in range(len(nums) - 1):
#             res = max(res, nums[i + 1] - nums[i])
#         return res

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:   return 0
        n_max, n_min = max(nums), min(nums)
        interval = (n_max - n_min) // (len(nums) - 1)
        if interval == 0:   return n_max - n_min
        n_bucks = (n_max - n_min) // interval + 1
        buckets = [[] for _ in range(n_bucks)]

        for i in nums:
            index = (i - n_min) // interval
            buckets[index].append(i)

        res = -float('inf')
        for i in range(n_bucks):
            if buckets[i]:
                for j in range(i + 1, n_bucks):
                    if buckets[j]:
                        res = max(res, min(buckets[j]) - max(buckets[i]))
                        break
        return res
