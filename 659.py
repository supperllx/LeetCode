class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        dd = collections.defaultdict(list)
        for i in nums:
            if queue := dd[i - 1]:  # walrus operator 
                shortest = heapq.heappop(queue)
                heapq.heappush(dd[i], shortest + 1)
            else:
                heapq.heappush(dd[i], 1)
        for queue in dd.values():
            if queue and queue[0] < 3:    return False
        return True
        