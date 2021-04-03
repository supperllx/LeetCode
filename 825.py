class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        arr = [0] * 121
        for age in ages:
            arr[age] += 1
        res = 0
        for i in range(1, 121):
            if arr[i]:
                downLimit = max(1, i // 2 + 7 + 1)
                upLimit = i - 1
                if i >= 15:
                    res += arr[i] * (arr[i] - 1)
                for j in range(downLimit, upLimit + 1):
                    res += arr[i] * arr[j]
        return res