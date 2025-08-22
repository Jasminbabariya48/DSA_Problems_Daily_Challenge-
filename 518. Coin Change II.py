class solution:
    def coinchange(self, amount: int, coins: list[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(len(coins)):
            for x in range(coins[i], amount + 1):
                dp[x] += dp[x - coins[i]]
        return dp[amount]
    
if __name__ == "__main__":
    sol = solution()
    print(sol.coinchange(6, [1, 2, 5]))