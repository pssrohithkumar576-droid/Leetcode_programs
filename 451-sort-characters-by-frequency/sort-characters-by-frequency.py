class Solution:
    def frequencySort(self, s: str) -> str:
           
        count = {}

        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        sorted_chars = sorted(
            count.items(),
            key=lambda x: x[1],
            reverse=True
        )

        result = ""

        for ch, freq in sorted_chars:
            result += ch * freq

        return result