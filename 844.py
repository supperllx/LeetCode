class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s1 = []
        s2 = []
        for i in S:
            if i == '#':
                if s1:
                    s1.pop()
            else:
                s1.append(i)
        for j in T:
            if j == '#':
                if s2:
                    s2.pop()
            else:
                s2.append(j)
        print(s1)
        print(s2)
        return s1 == s2