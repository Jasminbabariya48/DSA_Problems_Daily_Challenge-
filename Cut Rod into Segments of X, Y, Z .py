class solution:
    def cutRod(self, n: int, x: int, y: int, z: int) -> int:
        dp = [-1] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            for length in (x, y, z):
                if i >= length and dp[i - length] != -1:
                    dp[i] = max(dp[i], dp[i - length] + 1)

        return dp[n]
    
if __name__ == "__main__":
    sol = solution()
    n = 5
    x = 1
    y = 2
    z = 3
    print(sol.cutRod(n, x, y, z))