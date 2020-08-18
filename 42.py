class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 1:
            return 0
        left = 0
        right = len(height) - 1
        ans = 0
        lmax = height[left]
        rmax = height[right]

        while left <= right:
            if lmax <= rmax:
                lmax = max(lmax, height[left])
                ans +=  (lmax - height[left])
                left+=1
            else:
                rmax = max(rmax, height[right])
                ans +=  (rmax - height[right])
                right-=1

        return ans 