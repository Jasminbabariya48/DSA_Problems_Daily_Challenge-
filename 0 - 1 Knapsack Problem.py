from typing import List

class solution:
    def solver(self, capacity, val, wt, index, dp):
        if index == 0:
            if wt[0] <= capacity:
                return val[0]
            else:
                return 0

        if dp[index][capacity] != -1:
            return dp[index][capacity]

        include = 0

        exclude = self.solver(capacity, val, wt, index - 1, dp)

        
        if wt[index] <= capacity:
            include = val[index] + self.solver(capacity - wt[index], val, wt, index - 1, dp)

        dp[index][capacity] = max(include, exclude)
        return dp[index][capacity]

    def knapsack(self, W, val, wt):
        dp = [[-1 for _ in range(W + 1)] for _ in range(len(wt) + 1)]

        return self.solver(W, val, wt, len(wt)-1, dp)
    
if __name__ == "__main__":
    W = 50
    val = [60, 100, 120]
    wt = [10, 20, 30]
    knapsack = solution()
    print(knapsack.knapsack(W, val, wt))