class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        angry, happy = 0, 0
        left, right = 0, 0
        max_angry = 0
        while right < len(customers):
            if grumpy[right] == 1:
                angry += customers[right]
            else:
                happy += customers[right]
            while right - left + 1 > X:
                if grumpy[left] == 1:
                    angry -= customers[left]
                left += 1
            max_angry = max(max_angry, angry)
            right += 1
        return max_angry + happy