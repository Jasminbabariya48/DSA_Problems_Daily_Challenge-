class solution:
    def waytoreach(self, n):
        if n <= 1:
            return 1
        
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

if __name__ == "__main__":
    n = 5
    sol = solution()
    print(sol.waytoreach(n))