class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.sh_nums = nums.copy()
        

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums
        

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        n = len(self.sh_nums)
        for i in range(n):
            r = random.randint(i, n - 1)
            self.sh_nums[i], self.sh_nums[r] = self.sh_nums[r], self.sh_nums[i]
        return self.sh_nums


        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()