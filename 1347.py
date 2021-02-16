class Solution:
    def minSteps(self, s: str, t: str) -> int:
        arrS = [0] * 26
        for ch in s:
            arrS[ord(ch) - 97] += 1
        
        arrT = [0] * 26
        for ch in t:
            arrT[ord(ch) - 97] += 1
        
        diff = 0
        for i in range(26):
            diff += abs(arrS[i] - arrT[i])
        return diff >> 1
