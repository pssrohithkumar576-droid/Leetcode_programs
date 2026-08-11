class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        ans = 0

        while n > 1:
            mid = 2 ** (n - 2)

            if k > mid:
                k -= mid
                ans = 1 - ans

            n -= 1

        return ans