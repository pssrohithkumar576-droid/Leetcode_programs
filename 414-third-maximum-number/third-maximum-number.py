class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        d=list(set(tuple(nums)))
        d.sort()
        if len(d)<3:
            return max(d)
        else:
            return d[-3]