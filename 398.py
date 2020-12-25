# class Solution:

#     def __init__(self, nums: List[int]):
#         self.dd = collections.defaultdict(list)
#         for index, n in enumerate(nums):
#             self.dd[n].append(index)

#     def pick(self, target: int) -> int:
#         # r = random.randint(0, len(self.dd[target]) - 1)
#         # return self.dd[target][r]
#         return random.choice(self.dd[target])
        
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        count = 0
        res = -1
        for index, n in enumerate(self.nums):
            if n == target:
                count += 1
                r = random.randint(0, count - 1)
                if r == 0:
                    res = index
        return res
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)