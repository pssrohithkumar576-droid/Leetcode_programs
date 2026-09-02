class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        freq = {}
        window_sum = 0
        maxSum = 0
        left = 0

        for i in range(left,k):
            window_sum += nums[i]
            freq[nums[i]] = freq.get(nums[i],0) + 1

        if len(freq) == k:
            maxSum = window_sum

        for right in range(k,len(nums)):
            left = right - k
            window_sum -= nums[left]

            freq[nums[left]] -= 1

            if freq[nums[left]] == 0:
                del freq[nums[left]]

            window_sum += nums[right]
            freq[nums[right]] = freq.get(nums[right],0) + 1

            if len(freq) == k:
                maxSum = max(window_sum,maxSum)
        return maxSum