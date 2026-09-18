class Solution:
    def calPoints(self, operations: list[str]) -> int:
        st = []
        for i in operations:
            if i != 'C' and i != 'D' and i != '+':
                st.append(int(i))
            elif i == 'D':
                val = st[-1] * 2
                st.append(val)
            elif i == 'C':
                st.pop()
            elif i == '+':
                val1, val2 = st[-1], st[-2]
                st.append(val1 + val2)
        return sum(st)