class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = [i for i in s.split(' ') if i != '' ]
        return len(res[-1]) if len(res) > 0 else 0