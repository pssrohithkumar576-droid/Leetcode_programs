class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        Word1 = "".join(word1)
        Word2 = "".join(word2)
        return Word1 == Word2