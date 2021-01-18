# class Solution:
#     def maxNumberOfBalloons(self, text: str) -> int:
#         dd = collections.defaultdict(int)
#         for ch in text:
#             dd[ch] += 1
#         res = 0
#         while True:
#             for ch in 'balloon':
#                 dd[ch] -= 1
#                 if dd[ch] < 0:  return res
#             res += 1

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        s = {'a', 'b', 'l', 'n', 'o'}
        dd = collections.defaultdict(int)
        for ch in text:
            if ch in s: dd[ch] += 1
        # return min([(v if k not in {'l', 'o'} else v // 2) for k, v in dd.items()]) if len(dd) == 5 else 0
        return min(dd['a'], dd['b'], dd['l'] // 2, dd['n'], dd['o'] // 2)