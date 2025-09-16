import math
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        n = len(tokens)

        for i in range(n):
            if tokens[i].lstrip('-').isdigit():
                s.append(int(tokens[i]))
            else:
                b = s[-1]
                s.pop()
                a = s[-1]
                s.pop()

                if tokens[i] == '+':
                    s.append(a+b)
                elif tokens[i] == '-':
                    s.append(a-b)
                elif tokens[i] == '*':
                    s.append(a*b)
                else:
                    s.append(math.trunc(a/b))
        return s[-1]
        
if __name__ == "__main__":
    sol = Solution()
    tokens = ["2","1","+","3","*"]
    print(sol.evalRPN(tokens))