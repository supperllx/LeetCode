# class Solution:
#     def sortedSquares(self, A: List[int]) -> List[int]:
#         return sorted([i**2 for i in A])

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        for i in range(len(A)):
            if A[i] >= 0:  break
        neg = [j**2 for j in A[0:i]]
        neg.reverse()
        pos = [j**2 for j in A[i:]]
        pn, pp = 0, 0
        res = []
        while pn < len(neg) and pp < len(pos):
            if neg[pn] < pos[pp]:
                res.append(neg[pn])
                pn += 1
            else:
                res.append(pos[pp])
                pp += 1
        if pn == len(neg): res.extend(pos[pp:])
        elif pp == len(pos):   res.extend(neg[pn:])
        return res