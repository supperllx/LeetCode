class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # d = dict(zip(nums2, range(len(nums2))))
        # i2 = 0
        # for i1 in range(len(nums1)):
        #     n1 = nums1[i1]
        #     nums1[i1] = -1
        #     for i2 in range( d[n1],len(nums2) ):
        #         n2 = nums2[i2]
        #         if n2 > n1:
        #             nums1[i1] = n2
        #             break

            
        # return nums1

        if len(nums1) == 0:
            return nums1
        d = {}
        stack = []
        stack.append(nums2[0])
        for i in range(1, len(nums2)):
            # n1 = stack[-1]
            n2 = nums2[i]
            if len(stack) == 0:
                stack.append(nums2[i])
                continue
            if n2 <= stack[-1]:
                stack.append(nums2[i])
                continue
            while(len(stack) and n2 > stack[-1]):
                d[stack.pop()] = n2
            stack.append(n2)
        for j in range(len(nums1)):
            n1 = nums1[j]
            nums1[j] = d.get(n1, -1)
        return nums1
                
