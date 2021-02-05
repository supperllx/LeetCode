# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
#         arr = [0] * 26
#         left, right = 0, 0
#         res = 0
#         while right < len(s):
#             arr[ord(s[right]) - 65] += 1
#             if max(arr) + k >= right - left + 1:
#                 res = max(res, right - left + 1)
#                 right += 1
#             else:
#                 right += 1
#                 arr[ord(s[left]) - 65] -= 1
#                 left += 1
#         return res

# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
#         ct = collections.Counter()
#         left, right = 0, 0
#         res = 0
#         while right < len(s):
#             ct[s[right]] += 1
#             if ct.most_common(1)[0][1] + k < right - left + 1:
#                 ct[s[left]] -= 1
#                 left += 1
#             res = max(res, right - left + 1)
#             right += 1
#         return res

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        arr = [0] * 26
        left, right = 0, 0
        res = 0
        while right < len(s):
            arr[ord(s[right]) - 65] += 1
            if max(arr) + k < right - left + 1:
                arr[ord(s[left]) - 65] -= 1
                left += 1
            else:
                res = max(res, right - left + 1)
            right += 1
        return res