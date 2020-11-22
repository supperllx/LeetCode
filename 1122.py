class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d = {}
        n = len(arr1)
        for no, i in enumerate(arr2):    d[i] = no
        arr1.sort(key = lambda x: d[x] if x in d else x + n)
        return arr1