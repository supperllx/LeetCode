class Solution:
    def maxPower(self, s: str) -> int:
        maxLen = 0
        left, right = 0, 0
        curLen = 0
        while right < len(s):
            if s[right] == s[left]:
                maxLen = max(maxLen, right - left + 1)
            else:
                left = right
            right += 1
        return maxLen

