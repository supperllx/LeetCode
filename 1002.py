class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        res = []
        size = len(A)
        l = [[0 for _ in range(26)] for i in range(size)]
        for i in range(size):
            for ch in A[i]:
                index = ord(ch) - 97
                l[i][index] += 1
        for ch in range(26):
            count = float('inf')
            for j in range(size):
                count = min(count, l[j][ch])
            for c in range(count):
                res.append(chr(ch + 97))
        return res
