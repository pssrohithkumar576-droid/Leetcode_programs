class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        target = 0
        trplets = []
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                t = nums[i] + nums[left] + nums[right]
                if t > target:
                    right -= 1
                elif t < target:
                    left += 1
                else:
                    trplets.append((nums[i],nums[left],nums[right]))
                    left += 1
                    right -= 1
        return list(set(trplets))