# class Solution:
#     def trap(self, height: List[int]) -> int:
#         if len(height) <= 2:
#             return 0
#         left = 0
#         right = len(height) - 1
#         max_l = height[0]
#         max_r = height[-1]
#         res = 0
#         while left <= right:
#             if max_l < max_r:
#                 res += max_l - height[left]
#                 left += 1
#                 max_l = max(max_l, height[left])
#             if max_l >= max_r:
#                 res += max_r - height[right]
#                 right -= 1
#                 max_r = max(max_r, height[right])
#         return res

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n <= 1:
            return 0
        hp = []
        heapq.heappush(hp, (height[0], 0))
        heapq.heappush(hp, (height[n - 1], n - 1))
        height[0], height[n - 1] = -1, -1

        res = 0
        while hp:
            h, i = heapq.heappop(hp)
            for ni in (i - 1, i + 1):
                if 0 < ni < n - 1 and height[ni] >= 0:
                    if h > height[ni]:
                        res += (h - height[ni])
                    heapq.heappush(hp, (max(h, height[ni]), ni))
                    height[ni] = -1
        return res