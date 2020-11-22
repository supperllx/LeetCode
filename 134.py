# class Solution:
#     def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
#         arr = [gas[i] - cost[i] for i in range(len(gas))]
#         if sum(arr) < 0:    return -1
#         n = len(gas)
#         for i in range(n):
#             remain_gas = 0
#             for j in range(n):
#                 remain_gas += arr[i]
#                 if remain_gas < 0:  break
#                 i = (i + 1) % n
#             if j == n - 1:  return i
                
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        arr = [gas[i] - cost[i] for i in range(len(gas))]
        if sum(arr) < 0:    return -1
        n = len(gas)
        i = 0
        while i < n:
            remain_gas = 0
            for j in range(n):
                remain_gas += arr[i]
                i = (i + 1) % n
                if remain_gas < 0:  break
            if remain_gas >= 0:  return i