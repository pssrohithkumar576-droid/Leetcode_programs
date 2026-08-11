class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index = -1

        for i in range(len(word)):
            if word[i] == ch:
                index = i
                break

        if index == -1:
            return word

        return word[:index + 1][::-1] + word[index + 1:]