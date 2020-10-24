class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for row in A:
            row.reverse()
            for i in range(len(row)):
                row[i]^= 1
        return A