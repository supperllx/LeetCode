# class Solution:
#     def sortByBits(self, arr: List[int]) -> List[int]:
#         def transfer(n: int):
#             s = str(bin(n)[2:])
#             return (sum([int(i) for i in s]), n)
#         return sorted(arr, key = transfer)

# class Solution:
#     def sortByBits(self, arr: List[int]) -> List[int]:
#         def transfer(n: int):
#             res = 0
#             raw = n
#             while n:
#                 res += n%2
#                 n //= 2
#             return (res, raw)
#         return sorted(arr, key = transfer)
        
# class Solution:
#     def sortByBits(self, arr: List[int]) -> List[int]:
#         return sorted(arr, key = lambda x: (bin(x).count('1'), x))

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort(key = lambda x: (bin(x).count('1'), x))
        return arr