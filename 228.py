class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        path = []
        n = len(nums)
        for i in range(n):
            if not path or nums[i] - int(path[-1]) == 1:
                while len(path) > 1:    path.pop()
                # path.append(str(nums[i]))
            else:
                res.append('->'.join(path))
                path.clear()
                # path.append(str(nums[i]))
            path.append(str(nums[i]))
        if path:    res.append('->'.join(path))
        return res