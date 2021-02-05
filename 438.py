# class Solution:
#     def findAnagrams(self, s: str, p: str) -> List[int]:
#         if len(p) > len(s): return []
#         def sTOl(s):    
#             d = [0] * 26
#             for ch in s:
#                 d[ord(ch) - 97] += 1
#             return d
#         pl = sTOl(p)
#         sl = sTOl(s[0:len(p)])
#         res = []

#         left, right = 0, len(p) - 1
#         while right < len(s) - 1:
#             if sl == pl:    res.append(left)
#             sl[ord(s[left]) - 97] -= 1
#             left += 1
#             right += 1
#             sl[ord(s[right]) - 97] += 1
        
#         if sl == pl:    res.append(left)
            
#         return res

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        np = len(p)
        lp = [0] * 26
        for ch in p:
            lp[ord(ch) - 97] += 1
        ls = [0] * 26
        left, right = 0, 0
        res = []
        while right < len(s):
            ls[ord(s[right]) - 97] += 1
            if right - left + 1 > np:
                ls[ord(s[left]) - 97] -= 1
                left += 1
            if ls == lp:    res.append(left)
            right += 1
        return res
