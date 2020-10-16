class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        dp = [1]
        n_primes = len(primes)
        indexes = [0] * n_primes
        for _ in range(1, n):
            ugly = min([dp[indexes[i]] * primes[i] for i in range(n_primes) ])
            dp.append(ugly)
            for i in range(n_primes):
                if ugly == dp[indexes[i]] * primes[i]:  indexes[i] += 1
        return dp[-1]