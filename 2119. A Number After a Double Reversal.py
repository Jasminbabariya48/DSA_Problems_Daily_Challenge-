class Solution:
    def solve(self, A: int) -> int:
        str_A = str(A)
        reversed_str_A = str_A[::-1]
        double_reversed_str_A = reversed_str_A[::-1]
        
        if str_A == double_reversed_str_A:
            return 1
        else:
            return 0
        
if __name__ == "__main__":
    sol = Solution()
    print(sol.solve(12321))  # Output: 1
    print(sol.solve(12345))  # Output: 0