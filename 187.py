# class Solution:
#     def findRepeatedDnaSequences(self, s: str) -> List[str]:
#         if len(s) < 10: return []
#         c = collections.Counter()
#         res = []
#         for i in range(0, len(s) - 9):
#             string = s[i:i+10]
#             if c[string] == 1:  
#                 res.append(string)
#             c[string] += 1
#         return res

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ht = set()
        res = set()
        for i in range(0, len(s) - 9):
            string = s[i:i+10]
            temp = hash(string)
            if temp in ht: res.add(string)
            else:   ht.add(temp)
        return list(res)