class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        temp = 0
        for i in range(len(shifts) - 2, -1, -1):
            shifts[i] += shifts[i + 1]
        
        res = ''
        for i, ch in  enumerate(S):
            res += chr(97 + ((ord(ch) - 97) + (shifts[i] % 26)) % 26)
        return res