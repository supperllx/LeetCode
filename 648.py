class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        roots = set(dictionary)
        
        def replace(s):
            for i in range(len(s)):
                if (prefix := s[:i]) in roots:
                    return prefix
            return s
        
        return ' '.join(map(replace, sentence.split(' ')))
