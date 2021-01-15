class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dd = collections.defaultdict(list)
        for word in wordDict:   dd[word[0]].append(word)
        n = len(s)

        @functools.cache
        def dfs(i):
            nonlocal n, dd
            if i == n:  return True
            if s[i] not in dd:  return False
            temp_res = False
            for word in dd[s[i]]:
                l = len(word)
                if s[i:i + l] == word and dfs(i + l):
                    temp_res = True
                    break
            return temp_res
        return dfs(0)
        