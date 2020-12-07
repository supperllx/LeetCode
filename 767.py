class Solution:
    def reorganizeString(self, S: str) -> str:
        ct = collections.Counter(S)
        if ct.most_common(1)[0][1] > (len(S) + 1) // 2:    return ''
        hp = []
        for ch in ct.keys():
            heapq.heappush(hp, (-ct[ch], ch))

        res = ""
        while len(hp):
            first = heapq.heappop(hp)
            res += first[1]
            if len(hp):
                second = heapq.heappop(hp)
                res += second[1]
                if second[0] < -1:   heapq.heappush(hp, (second[0] + 1, second[1]))
            if first[0] < -1:    heapq.heappush(hp, (first[0] + 1, first[1]))
        return res
                            