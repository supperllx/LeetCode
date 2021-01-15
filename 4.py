class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float: # O(n)
        i1, i2 = 0, 0
        l1, l2 = len(nums1), len(nums2)
        total = l1 + l2
        mid = total // 2 + 1
        cache = collections.deque(maxlen = 2)
        while mid:
            if i1 < l1 and i2 < l2:
                if nums1[i1] <= nums2[i2]:
                    cache.append(nums1[i1])
                    i1 += 1
                else:
                    cache.append(nums2[i2])
                    i2 += 1
            else:
                if i1 == l1:
                    cache.append(nums2[i2])
                    i2 += 1
                elif i2 == l2:
                    cache.append(nums1[i1])
                    i1 += 1
            mid -= 1
        return cache[-1] if total % 2 == 1 else sum(cache) / 2
