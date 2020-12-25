# class Solution:
#     def findContentChildren(self, g: List[int], s: List[int]) -> int:
#         g.sort()
#         s.sort()
#         child = 0
#         cookie = 0
#         res = 0
#         while child < len(g) and cookie < len(s):
#             if s[cookie] >= g[child]:
#                 res += 1
#                 child += 1
#             cookie += 1
#         return res

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        res = 0
        cookie = 0
        for child in g:
            while cookie < len(s):
                if s[cookie] >= child:
                    res += 1
                    cookie += 1
                    break
                cookie += 1
        return res
