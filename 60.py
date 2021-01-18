class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def permuate(arr):
            length = len(arr)
            i = length - 2
            while i >= 0 and arr[i] >= arr[i + 1]:  i -= 1
            if i >= 0:
                j = length - 1
                while j >= 0 and arr[j] <= arr[i]:  j -= 1
                arr[i], arr[j] = arr[j], arr[i]
            
            left, right = i + 1, length - 1
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
        
        nums = list(range(1, n + 1))
        for i in range(k - 1):
            permuate(nums)
        return ''.join(map(str, nums))