# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         res = digits[::-1]
#         res[0] += 1
#         for i in range(len(res)):
#             if res[i] == 10:
#                 res[i] = 0
#                 if i + 1 < len(res):    res[i + 1] += 1
#                 else:   res.append(1)
#         return res[::-1]

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 10:
                digits[i] = 0
                if i - 1 >= 0:    digits[i - 1] += 1
                else:   digits.insert(0, 1)
        return digits