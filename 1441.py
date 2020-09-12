class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        index = 0
        res = []
        for i in range(1, n+1):
            if i == target[index]:
                res.append('Push')
                index += 1
            else:
                res.append('Push')
                res.append('Pop')
            if index == len(target):
                break
        return res