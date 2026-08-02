class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        read = 0
        write = 0
        for i in range(len(nums)):
            if nums[read] == nums[write]:
                read = read + 1
            else:
                write = write + 1
                nums[write] = nums[read]
                read = read + 1
        return write + 1