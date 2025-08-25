from typing import List

class Solution:
    def solver(self, index, buy, prices, limit, dp):
        if index == len(prices):
            return 0
            
        if limit == 0:
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
            skpikaro = 0 + self.solver(index+1, 0, prices, limit, dp) 
            profit = max(sellkaro, skpikaro)
            
        dp[index][buy][limit] = profit
        return profit
                
    
    
    def maxProfit(self, prices):
        n = len(prices)
        dp = [[[-1 for _ in range(3)] for _ in range(2)] for _ in range(n)]
        return self.solver(0, 1, prices, 2, dp)
    
if __name__ == "__main__":
    prices = [3,2,6,5,0,3]
    solution = Solution()
    print(solution.maxProfit(prices))