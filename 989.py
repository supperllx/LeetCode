class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        temp = int(''.join(map(str, A)))
        return [i for i in str(temp + K)]