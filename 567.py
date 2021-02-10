class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Len = len(s1)
        arr = [0] * 26
        for ch in s1:
            arr[ord(ch) - 97] += 1
        
        window = [0] * 26
        left, right = 0, 0
        while right < len(s2):
            window[ord(s2[right]) - 97] += 1
            while right - left + 1 > s1Len:
                window[ord(s2[left]) - 97] -= 1
                left += 1
            if arr == window:
                return True
            right += 1
        return False