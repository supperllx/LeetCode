# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         def sTOhash(s):
#             array = [0] * 26
#             for ch in s:
#                 array[ord(ch) - 97] += 1
#             return hash(str(array))
        
#         d = {}
#         for string in strs:
#             temp = sTOhash(string)
#             if temp in d:   d[temp].append(string)
#             else:   d[temp] = [string]
#         return list(d.values())

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)
        for string in strs:
            count = [0]*26
            for ch in string:   count[ord(ch) - 97] += 1
            d[hash(str(count))].append(string)
        return list(d.values())