class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningsum=[]
        sum=0
        for i in range(len(nums)):
            sum=sum+nums[i]
            runningsum.append(sum)
        return runningsum