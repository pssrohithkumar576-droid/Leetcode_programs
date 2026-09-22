class Solution:
    def convertDateToBinary(self, date: str) -> str:
        a = date.split("-")
        b = [bin(int(x))[2:] for x in a]
        return "-".join(b)