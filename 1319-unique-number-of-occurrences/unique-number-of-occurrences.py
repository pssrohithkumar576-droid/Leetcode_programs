class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = {}

        for num in arr:
            count[num] = count.get(num, 0) + 1

        frequencies = count.values()

        return len(frequencies) == len(set(frequencies))