# class Solution:
#     def numRabbits(self, answers: List[int]) -> int:
#         total = 0
#         ct = collections.Counter(answers)
#         for num, count in ct.items():
#             if num == 0:    total += count
#             elif count % (num + 1) == 0:    total += count
#             else:   total += (count // (num + 1) + 1) * (num + 1)
#         return total

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        total = 0
        ct = collections.Counter(answers)
        for num, count in ct.items():
            if num == 0:    total += count
            else:   total += math.ceil(count / (num + 1)) * (num + 1)
        return total