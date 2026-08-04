class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        c = max(nums)
        b = min(nums)
        a =[]
        for i in range(b,c+1):
            if i not in nums:
                a.append(i)
        return a