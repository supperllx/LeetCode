class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        arr1 = version1.split('.')
        arr2 = version2.split('.')
        n = max(len(arr1), len(arr2))
        for i in range(n):
            v1 = arr1[i] if i < len(arr1) else '0'
            v2 = arr2[i] if i < len(arr2) else '0'
            if int(v1) < int(v2):   return -1
            elif int(v1) > int(v2): return 1
        return 0