class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        A = nums[:(len(nums) + 1) // 2]
        B = nums[(len(nums) + 1) // 2:]
        nums.clear()
        while A and B:
            nums.append(A.pop())
            nums.append(B.pop())
        nums.extend(A)
