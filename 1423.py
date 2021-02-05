# class Solution:
#     def maxScore(self, cardPoints: List[int], k: int) -> int:
#         @functools.cache
#         def func(left, right, k):
#             if k == 1:
#                 return max(cardPoints[left], cardPoints[right])
#             else:
#                 lv = cardPoints[left] + func(left + 1, right, k - 1)
#                 rv = cardPoints[right] + func(left, right - 1, k - 1)
#                 return max(lv, rv)
#         return func(0, len(cardPoints) - 1, k)

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        window_length = len(cardPoints) - k
        window_min = float('inf')
        left, right = 0, 0
        curSum = 0
        while right < len(cardPoints):
            curSum += cardPoints[right]
            if right - left + 1 > window_length:
                curSum -= cardPoints[left]
                left += 1
            if right - left + 1 == window_length:
                window_min = min(window_min, curSum)
            right += 1
        return sum(cardPoints) - window_min

