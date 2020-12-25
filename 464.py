class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if maxChoosableInteger >= desiredTotal: return True
        if (1 + maxChoosableInteger) * maxChoosableInteger / 2 < desiredTotal:  return False

        @functools.cache
        def dfs(used, target):
            for i in range(maxChoosableInteger):
                cur_encoded = 1 << i
                if cur_encoded & used == 0:
                    n = i + 1
                    if n >= target or not dfs(cur_encoded | used, target - n):
                        return True
            return False
        
        return dfs(0, desiredTotal)