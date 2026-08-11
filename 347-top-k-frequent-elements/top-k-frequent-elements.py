class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for num in nums:
            if num in count.keys():
                count[num] += 1
            else:
                count[num] = 1
        ans = sorted(count.items(),key=lambda t:t[1],reverse=True)
        output = [ans[i][0] for i in range(k)]
        return output