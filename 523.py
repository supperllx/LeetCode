class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d = dict()
        temp = 0
        d[0] = -1
        for index, n in enumerate(nums):
            temp += n
            if k != 0:  temp %= k
            if temp not in d:
                d[temp] = index
            elif index - d[temp] > 1:
                return True
        return False