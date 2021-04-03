class Solution:
    def reverseVowels(self, s: str) -> str:
        stack = []
        d = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        for ch in s:
            if ch in d: stack.append(ch)
        
        res = ''
        for ch in s:
            if ch not in d: res += ch
            else:   res += stack.pop()
        return res