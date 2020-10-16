class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        ct = collections.Counter()
        for i in arr:
            ct[i] += 1
        return len(ct.keys()) == len(set(ct.values()))