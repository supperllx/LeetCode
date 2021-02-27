# class Solution:
#     def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
#         ctS = collections.Counter(map(str.lower, filter(str.isalpha, licensePlate)))
#         res = [float('inf'), '']
#         for word in words:
#             ctW = collections.Counter(word)
#             isSub = True
#             for ch in ctS.keys():
#                 if ctS[ch] > ctW[ch]:
#                     isSub = False
#                     break
#             if isSub and (n := len(word)) < res[0]:
#                 res[0], res[1] = n, word
#         return res[1]

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        ctS = collections.Counter(map(str.lower, filter(str.isalpha, licensePlate)))
        res = 0
        words.sort(key = lambda s: len(s))
        for word in words:
            ctW = collections.Counter(word)
            isSub = True
            for ch in ctS.keys():
                if ctS[ch] > ctW[ch]:
                    isSub = False
                    break
            if isSub:
                return word