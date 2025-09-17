from typing import List

class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        n = len(s)

        for i in range(n):
            if s[i] != ']':
                st.append(s[i])
 
            else:
                temp = []
                while st and st[-1] != '[':
                    temp.append(st.pop())
                st.pop()
                temp.reverse()

                nums = []
                while st and st[-1].isdigit():
                    nums.insert(0, st.pop())
                    
                numbers = int("".join(nums))
                
                repet = "".join(temp) * numbers
                
                st.extend(repet)

        return "".join(st)
    
if __name__ == "__main__":
    sol = Solution()
    s = "3[a]2[bc]"
    print(sol.decodeString(s))