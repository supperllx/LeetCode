class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def func(k):
            res = [1] * (k + 1)
            if k <= 1:  return res
            else:
                path = func(k - 1)
                for i in range(1, k):
                    res[i] = path[i - 1] + path[i]
                return res
        return func(rowIndex)