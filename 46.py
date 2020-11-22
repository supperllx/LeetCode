class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def func(arr, path):
            nonlocal res
            if len(arr) == 0:   res.append(path)
            else:
                for i in range(len(arr)):
                    func(arr[:i] + arr[i+1:], path + [arr[i]])
        res = []
        func(nums, [])
        return res