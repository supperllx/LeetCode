class Solution:
    def candy(self, ratings: List[int]) -> int:
        if not ratings: return 0
        n = len(ratings)
        
        left2right = [1] * n
        right2left = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                left2right[i] = left2right[i - 1] + 1
            else:   left2right[i] = 1
            if ratings[n - 1 - i] > ratings[n - 1 - i + 1]:
                right2left[n - 1 - i] = right2left[n - 1 - i + 1] + 1
            else:   right2left[n - 1 - i] = 1
        res = 0
        for i in range(n):
            res += max(left2right[i], right2left[i])
        return res