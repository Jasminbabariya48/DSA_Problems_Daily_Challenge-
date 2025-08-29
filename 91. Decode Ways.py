class Solution:
    def solver(self, index, n, s, dp): # pyright: ignore[reportUnknownParameterType]
        if index == n:
            return 1
        if s[index] == '0':
            return 0
        if dp[index] != -1:
            return dp[index]
        count = self.solver(index + 1, n, s, dp)
        if index + 1 < n and int(s[index:index + 2]) <= 26:
            count += self.solver(index + 2, n, s, dp)
        dp[index] = count
        return count

    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [-1] * n
        dp[0] = self.solver(0, n, s, dp)

        return dp[0]
    
if __name__ == "__main__":
    solution = Solution()
    test_string = "226"
    print(solution.numDecodings(test_string))