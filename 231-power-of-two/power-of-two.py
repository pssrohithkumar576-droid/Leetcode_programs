class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        #keep dividing by 2
        #if finally you get 1 . then it is a power of 2
        if n<=0:
            return False
        while n%2 == 0:
            n//=2
        return n==1      