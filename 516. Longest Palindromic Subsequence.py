class solution:
    def longestpalindromicSubsequence(self, s: str) -> int:
        # DP IN Tabulation
        s2 = s[::-1]
        dp = [[0] * (len(s2) + 1) for _ in range(len(s) + 1)]

        for i in range(len(s)-1,-1,-1):
            for j in range(len(s2)-1,-1,-1):
                ans = 0

                if s[i] == s2[j]:
                    ans = 1 + dp[i + 1][j + 1]

                else:
                    ans = max(dp[i + 1][j], dp[i][j + 1])
                dp[i][j] = ans
        return dp[0][0]

if __name__ == "__main__":
    solution = solution()
    s = "bbabcbcab"
    print(solution.longestpalindromicSubsequence(s))  # Output: 7