from typing import List

class Solution:
    def solver(self, index, buy, prices, limit, dp):
        if index == len(prices) or limit == 0:
            return 0
            
        if dp[index][buy][limit] != -1:
            return dp[index][buy][limit]
            
        profit = 0
        
        if buy:
            buykaro = -prices[index] + self.solver(index+1, 0, prices, limit, dp)
            skipkaro = 0 + self.solver(index+1, 1, prices, limit, dp)
            profit = max(buykaro, skipkaro)
            
        else:
            sellkaro = prices[index] + self.solver(index+1, 1, prices, limit-1, dp)
            skipkaro = 0 + self.solver(index+1, 0, prices, limit, dp)
            profit = max(sellkaro, skipkaro)
            
        dp[index][buy][limit] = profit
        return profit 

    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[-1 for _ in range(k+1)]for _ in range(2)] for _ in range(n)]
        return self.solver(0, 1, prices, k, dp)
    
if __name__ == "__main__":
    sol = Solution()
    k = 2
    prices = [3,2,6,5,0,3]
    print(sol.maxProfit(k, prices))