class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        def func(arr, path):
            nonlocal res
            if len(arr):
                for i in range(len(arr)):
                    res.append(path + [arr[i]])
                    func(arr[i + 1:], path + [arr[i]])
        func(nums, [])
        return res
                