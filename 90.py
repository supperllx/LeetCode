class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        s = set()
        n = len(nums)
        nums.sort()
        def func(i: int, path: tuple):
            nonlocal s
            if i == n:
                s.add(path)
            else:
                for j in range(i, n):
                    if j > i and nums[j] == nums[j - 1]:    continue
                    cur = nums[j]
                    s.add(path + (cur, ))
                    func(j + 1, path + (cur, ))
        
        func(0, ())
        return [list(v) for v in s] + [[]]