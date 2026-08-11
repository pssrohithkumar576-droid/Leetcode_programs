class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        white_count = 0

        for i in range(k):
            if blocks[i] == 'W':
                white_count += 1

        ans = white_count

        for right in range(k, len(blocks)):
            
            if blocks[right] == 'W':
                white_count += 1

            left = right - k

            if blocks[left] == 'W':
                white_count -= 1

            ans = min(ans, white_count)

        return ans