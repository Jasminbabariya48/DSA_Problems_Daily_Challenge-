from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        mini = prices[0]
        profit = 0

        for i in range(n):
            dif = prices[i] - mini
            profit = max(profit, dif)
            mini = min(mini, prices[i])
        return profit
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit([7,1,5,3,6,4]))
        