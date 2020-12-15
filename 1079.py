# class Solution:
#     def numTilePossibilities(self, tiles: str) -> int:
#         d = set()
#         def func(s, path):
#             nonlocal d
#             d.add(path)
#             if len(s):
#                 for i in range(len(s)):
#                     d.add(s[i])
#                     func(s[:i] + s[i+1:], path + s[i])
#         func(tiles, '')
#         return len(d) - 1

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        ct = collections.Counter(tiles)
        d = set()
        def func(path):
            nonlocal d
            if len(path) == len(tiles):   d.add(path)
            elif len(path) >= 0:
                nonlocal ct
                for ch in ct.keys():
                    if ct[ch] > 0:
                        ct[ch] -= 1
                        new_path = path + ch
                        d.add(new_path)
                        func(new_path)
                        ct[ch] += 1
        func('')
        return len(d)
                    