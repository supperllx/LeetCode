class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word in {word.upper(), word.lower(), word.capitalize()}
        # return word.islower() or word.isupper() or word.istitle()