import sortedcontainers
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        n, r = divmod(len(nums), k)
        if r:   return False
        ct = sortedcontainers.SortedDict()
        for n in nums:
            if n not in ct: ct[n] = 1
            else:   ct[n] += 1
        
        while ct:
            # base = ct.keys()[0]
            base = min(ct)
            for i in range(k):
                curNum = base + i
                if curNum not in ct:    return False
                else:
                    ct[curNum] -= 1
                    if ct[curNum] == 0:
                        ct.pop(curNum)
        return True