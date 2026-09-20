class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        d = {}
        for i in range(len(stones)):
            d[stones[i]] = d.get(stones[i],0) + 1
        count = 0
        for key,value in d.items():
            if key in jewels:
                count += value
        return count