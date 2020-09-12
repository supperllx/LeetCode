class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        res = []
        for i in nums1:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        for j in nums2:
            if j in d and d[j] > 0:
                res.append(j)
                d[j] -= 1
                
        return res