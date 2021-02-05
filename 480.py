# class Solution:
#     def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
#         left = [] # max heap
#         right = [] # min heap
#         median = None

#         def balance():
#             nonlocal left,right
#             while len(left) > len(right):
#                 heapq.heappush(right, -heapq.heappop(left))
#             while len(right) - len(left) > 1:
#                 heapq.heappush(left, -heapq.heappop(right))


#         def addElement(n):
#             nonlocal left, right, median
#             if not left and not right:  heapq.heappush(right, n)
#             elif n < median:
#                 heapq.heappush(left, -n)
#             elif n >= median:
#                 heapq.heappush(right, n)
#             balance()
#             median = right[0] if ((len(left) + len(right)) & 1) == 1 else (right[0] - left[0]) / 2
        
#         def deleteElement(n):
#             nonlocal left, right, median
#             # if n < median:
#             #     left.remove(-n)
#             # else:
#             #     right.remove(n)
#             if -n in left:
#                 left.remove(-n)
#                 heapq.heapify(left)
#             elif n in right:
#                 right.remove(n)
#                 heapq.heapify(right)
#             balance()
#             if len(left) + len(right) == 0: median = None
#             else:   median = right[0] if ((len(left) + len(right)) & 1) == 1 else (right[0] - left[0]) / 2

#         for i in range(k):
#             addElement(nums[i])

#         res = [median]
#         pLeft, pRight = 1, k
#         while pRight < len(nums):
#             deleteElement(nums[pLeft - 1])
#             addElement(nums[pRight])
#             res.append(median)
#             # print(left, right)
#             pLeft += 1
#             pRight += 1
#         return res

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        window = sorted(nums[:k])
        getMedian = lambda arr: (arr[(len(arr) - 1) // 2] + arr[len(arr) // 2]) / 2
        res = [getMedian(window)]
        for n_left, n_right in zip(nums[:-k], nums[k:]):
            window.pop(bisect.bisect_left(window, n_left))
            bisect.insort(window, n_right)
            res.append(getMedian(window))
        return res
