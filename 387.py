# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         od = collections.OrderedDict()
#         for i in range(len(s)):
#             ch = s[i]
#             if ch in od:    od[ch].append(i)
#             else:   od[ch] = [i]
        
#         for j in od.keys():
#             if len(od[j]) == 1: return od[j][0]
#         return -1

class Solution:
    def firstUniqChar(self, s: str) -> int:
        ct = collections.Counter(s)
        for i in range(len(s)):
            if ct[s[i]] == 1: return i
        return -1
