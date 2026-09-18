class Solution:
    def removeDuplicates(self, s: str) -> str:
        st = []
        for i in s:
            if not st:  # if stack is empty -> push
                st.append(i)
            else:
                if st[-1] == i: # Found a duplicate adjacent
                    st.pop()
                else:
                    st.append(i)
        return "".join(st)