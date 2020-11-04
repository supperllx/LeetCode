class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ct = collections.Counter(nums)
        arr = sorted(list(set(nums)))
        d = {}
        d[arr[0]] = 0
        for i in range(1, len(arr)):
            d[arr[i]] = d[arr[i - 1]] + ct[arr[i - 1]]
        return [d[i] for i in nums]
        