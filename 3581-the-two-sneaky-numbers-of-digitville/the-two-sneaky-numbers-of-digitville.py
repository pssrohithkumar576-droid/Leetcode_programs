class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = d.get(nums[i],0) + 1
        lst = []
        for key,value in d.items():
            if value == 2:
                lst.append(key)
        return lst