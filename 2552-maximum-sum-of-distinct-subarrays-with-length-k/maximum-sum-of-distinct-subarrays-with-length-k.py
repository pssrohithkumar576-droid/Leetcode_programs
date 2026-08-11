class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:

        count = {}
        current_sum = 0
        answer = 0

        for right in range(len(nums)):

            num = nums[right]
            current_sum += num
            count[num] = count.get(num, 0) + 1

            if right >= k:
                left_num = nums[right - k]

                current_sum -= left_num
                count[left_num] -= 1

                if count[left_num] == 0:
                    del count[left_num]

            if len(count) == k:
                answer = max(answer, current_sum)

        return answer