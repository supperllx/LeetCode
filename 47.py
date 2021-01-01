class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = set()
        def func(arr, path):
            if len(arr) == 1:
                nonlocal res
                if (temp := tuple(path + arr)) not in res:
                    res.add(temp)
            else:
                for i in range(len(arr)):
                    func(arr[:i] + arr[i+1: ], path + [arr[i]])
        func(nums, [])
        return [list(i) for i in res]
