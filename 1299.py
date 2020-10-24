class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        temp = -1
        for i in range(-1, -len(arr) - 1, -1):
            n,arr[i] = arr[i], temp
            temp = max(temp, n)
        return arr