class Solution:
    def majorityElement(self, nums: List[int]) -> int: # Boyer–Moore majority vote algorithm
        major = None
        count = 0
        for i in nums:
            if count == 0:  major = i
            if major == i:  count += 1
            else:   count -= 1
        return major