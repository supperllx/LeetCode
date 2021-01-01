class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def func(arr, last_sum, path):
            nonlocal res
            if len(arr) and last_sum < target:
                for i in range(len(arr)):
                    if last_sum + arr[i] == target:
                        res.append(path + [arr[i]])
                    func(arr[i:], last_sum + arr[i], path + [arr[i]])
        func(candidates, 0, [])
        return res