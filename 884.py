# class Solution:
#     def uncommonFromSentences(self, A: str, B: str) -> List[str]:
#         ctA, ctB = collections.Counter(A.split(' ')), collections.Counter(B.split(' '))
#         res = []

#         for w in ctA.keys():
#             if ctA[w] == 1 and w not in ctB:
#                 res.append(w)
#         for w in ctB.keys():
#             if ctB[w] == 1 and w not in ctA:
#                 res.append(w)
#         return res

class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        ct = collections.Counter(A.split(' ') + B.split(' '))
        res = []
        for w in ct.keys():
            if ct[w] == 1:
                res.append(w)
        return res