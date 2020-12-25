class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        ct = collections.Counter(s)
        stack = []
        record = set()
        for ch in s:
            ct[ch] -= 1
            if not len(stack):
                stack.append(ch)
                record.add(ch)
            elif ch not in record:
                while len(stack) and stack[-1] > ch and ct[stack[-1]] > 0:
                    record.remove(stack[-1])
                    stack.pop()
                stack.append(ch)
                record.add(ch)
        return ''.join(stack)
            
