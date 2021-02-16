class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def func(s):
            head, content = s.split(' ', 1)
            if content[0].isalpha():
                return (0, content, head)
            else:
                return (1, 0, 0)
        return sorted(logs, key = func)