class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        # ct = collections.defaultdict(int)
        increase = 0
        maxGain = 0
        fix = 0
        left, right = 0, 0
        while right < len(customers):
            if grumpy[right] == 1:
                increase += customers[right]
            else:
                fix += customers[right]
            while right - left + 1 > X:
                if grumpy[left] == 1:
                    increase -= customers[left]
                left += 1
            maxGain = max(maxGain, increase)
            right += 1
        return fix + maxGain