class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        curMax = max(candies)
        return [(c + extraCandies) >= curMax for c in candies]