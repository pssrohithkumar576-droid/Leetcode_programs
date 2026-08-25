class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        lst = []
        for i in order:
            if i in friends:
                lst.append(i)
        return lst       