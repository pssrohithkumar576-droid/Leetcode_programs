class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = 0
        max_length = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                left = right + 1
            else:
                max_length = max(max_length, right - left + 1)
                
        return max_length