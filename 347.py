class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        d = {}
        hp = []
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
                
        # for i in d:
        #     hp.append((-d[i], i))
        # heapify(hp)
        # return [heappop(hp)[1] for i in range(k)]
        
        for i in d:
            if len(hp) < k:
                heappush(hp, (d[i], i))
            else:
                heappushpop(hp, (d[i], i))
        return [i[1] for i in hp]

