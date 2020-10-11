class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:  return 0
        record = [1 for _ in range(n)]
        record[0], record[1] = 0, 0
        for i in range(2, n):
            record[i*2:n:i] = [0] * len(record[i*2:n:i])
        return sum(record)
        