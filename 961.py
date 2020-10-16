class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        ct = collections.Counter()
        dd = collections.defaultdict(set)
        for i in A:
            dd[ct[i]].discard(i)
            ct[i] += 1
            dd[ct[i]].add(i)
        return dd[len(A)//2].pop()