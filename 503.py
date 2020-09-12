class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        index = 0
        stack = []
        length = len(nums)
        ans = [-1]*length
        for i in range(2*length -1):
            index = i%length
            while len(stack) != 0 and nums[stack[-1]] < nums[index]:
                ans[stack.pop()] = nums[index]
            stack.append(index)
        return ans