class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def check(word):
            wTop = dict()
            pTow = dict()
            for chw, chp in zip(word, pattern):
                if chw not in wTop and chp not in pTow:
                    wTop[chw] = chp
                    pTow[chp] = chw
                elif chw in wTop and chp in pTow and wTop[chw] == chp and pTow[chp] == chw:
                    continue
                else:
                    return False
            return True

        return filter(check, words)