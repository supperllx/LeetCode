class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        n = len(customers)
        total = 0
        lastEstimateFinish = 0
        for arrival, time in customers:
            curEstimateFinish = max(lastEstimateFinish, arrival) + time
            curWait = curEstimateFinish - arrival
            total += curWait
            lastEstimateFinish = curEstimateFinish
        return total / n
