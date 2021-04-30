class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left, right = max(weights), sum(weights)
        def func(capacity):
            curLoad = 0
            d = 0
            for w in weights:
                if curLoad + w > capacity:
                    d += 1
                    curLoad = 0
                curLoad += w
            d += 1
            return d
        
        while left < right:
            mid = (left + right) // 2
            if func(mid) <= D:
                right = mid
            else:
                left = mid + 1
        return right # left will equal to right