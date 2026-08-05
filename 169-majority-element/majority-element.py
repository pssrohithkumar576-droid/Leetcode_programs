class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        for i in nums:
            if i in counts.keys():
                counts[i] += 1
            else:
                counts[i] = 1
        for key,value in counts.items():
            if value > len(nums)//2:
                return key