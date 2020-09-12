class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) == 0 or len(height) == 1:
            return 0
        left = 0
        right = len(height) - 1
        v = (right - left)*(height[left] if height[left] <= height[right] else height[right])

        while left < right:
            if height[left] < height[right]:
                left += 1
        
            else:
                right -= 1

            v_temp = (right - left)*(height[left] if height[left] <= height[right] else height[right])
            v = v if v > v_temp else v_temp

        return v