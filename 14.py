# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         if not strs:    return ''
#         shortest, longest = min(strs), max(strs)
#         res = ''
#         for i in range(len(shortest)):
#             if shortest[i] == longest[i]:   res += shortest[i]
#             else:   break
#         return res

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        temp = []
        for chs in zip(*strs):
            temp.append(set(chs))
        res = ''
        for s in temp:
            if len(s) > 1:  break
            res += s.pop()
        return res