class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zerosCount = 0
        maxLength = 0
        left = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zerosCount += 1
            while zerosCount > k:
                if nums[left] == 0:
                    zerosCount -= 1
                left += 1
            maxLength = max(maxLength,right - left + 1)
        return maxLength