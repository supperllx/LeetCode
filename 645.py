# class Solution:
#     def findErrorNums(self, nums: List[int]) -> List[int]:
#         ct = collections.Counter(nums)
#         n = ct.most_common(1)[0][0]
#         return [n, (collections.Counter([i for i in range(1, len(nums) + 1)]) - ct).most_common(1)[0][0]]

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        temp = sum(set(nums))
        n = len(nums)
        return [sum(nums) - temp, (n*(n + 1))//2 - temp ]