# class Solution:
#     def largestRectangleArea(self, heights: List[int]) -> int:
#         if not heights: return 0
#         n = len(heights)
#         left2right = [0] * n
#         right2left = [0] * n
#         stack = []
#         for i in range(n):
#             while stack and heights[stack[-1]] >= heights[i]:
#                 stack.pop()
#             left2right[i] = stack[-1] if stack else -1
#             stack.append(i)
#         stack.clear()
#         for i in range(n - 1, -1, -1):
#             while stack and heights[stack[-1]] >= heights[i]:
#                 stack.pop()
#             right2left[i] = stack[-1] if stack else n
#             stack.append(i)
#         return max([heights[i] * (right2left[i] - left2right[i] - 1) for i in range(n)])

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        if not n:   return 0
        left2right = [0] * n
        right2left = [0] * n
        l_stack = []
        r_stack = []
        for i in range(n):
            while len(l_stack) and heights[l_stack[-1]] >= heights[i]:
                l_stack.pop()
            left2right[i] = l_stack[-1] if l_stack else -1
            l_stack.append(i)

            r_i = n - 1 - i
            while len(r_stack) and heights[r_stack[-1]] >= heights[r_i]:
                r_stack.pop()
            right2left[r_i] = r_stack[-1] if r_stack else n
            r_stack.append(r_i)
        
        return max([heights[i] * (right2left[i] - left2right[i] - 1) for i in range(n)])
        # res = 0
        # for i in range(n):
        #     res = max(res, heights[i] * (right2left[i] - left2right[i] - 1))
        # return res

