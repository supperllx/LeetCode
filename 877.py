class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # @functools.lru_cache(None)
        @functools.cache
        def func(left, right):
            nonlocal piles
            if left == right:
                return piles[left]
            else:
                pick_left = piles[left] - func(left + 1, right)
                pick_right = piles[right] - func(left, right - 1)
                return max(pick_left, pick_right)
        return func(0, len(piles) - 1) > 0
