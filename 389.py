# class Solution:
#     def findTheDifference(self, s: str, t: str) -> str:
#         def getSum(s):
#             res = 0
#             for ch in s:    res += ord(ch)
#             return res
#         return str(chr(getSum(t) - getSum(s)))

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        res = 0
        for ch in s:
            res ^= ord(ch)
        for ch in t:
            res ^= ord(ch)
        return chr(res)