class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        arr = [i for i, s in enumerate(seats) if s == 1]
        if arr[0] - 0 > len(seats) - 1 - arr[-1]:
            maxInterval = arr[0] - 0
        else:
            maxInterval = len(seats) - 1 - arr[-1]
        for i in range(1, len(arr)):
            maxInterval = max(maxInterval, (arr[i] - arr[i - 1]) // 2)
        return maxInterval