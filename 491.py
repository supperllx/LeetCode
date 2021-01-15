class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = set()
        def func(arr, path):
            nonlocal res
            if len(arr) == 1:
                if not path:    return
                elif arr[0] >= path[-1]:
                    res.add(tuple(path + arr))
            else:
                for i in range(len(arr)):
                    if not path:
                        func(arr[i+1:], path + [arr[i]])
                    elif arr[i] >= path[-1]:
                        res.add(tuple(path + [arr[i]]))
                        func(arr[i+1: ], path + [arr[i]])
        func(nums, [])
        return [list(i) for i in res]