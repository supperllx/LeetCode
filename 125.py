class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:   return True
        # ts = [i.lower() for i in s if i.isalnum()]
        ts = [i.lower() for i in filter(str.isalnum, s)]
        # mid = len(ts) // 2
        # return ts[:mid] == ts[mid:][::-1] or ts[:mid] == ts[mid + 1:][::-1]
        return ts == ts[::-1]