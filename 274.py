class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # if len(citations) == 0: return 0
        citations.sort(reverse = True)
        res = 0
        for i in range(len(citations)):
            if citations[i] >= i + 1:  res += 1
            else:   break
        return res