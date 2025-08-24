from typing import List

class solution:
    def subset(self, n: int, sum: int, arr: List[int], dp: List[List[int]]) -> int:
        if sum < 0:
            return 0
        if sum == 0:
            return 1
        if n <= 0:
            return 0
        if dp[n][sum] != -1:
            return dp[n][sum]
        dp[n][sum] = self.subset(n-1, sum-arr[n-1], arr, dp) or self.subset(n-1, sum, arr, dp)
        return dp[n][sum]


    def issubsetsum(self, arr: List[int]) -> int:
        n = len(arr)
        sum = 0

        for i in range(n):
            sum += arr[i]

        if sum % 2 != 0:
            return False

        sum = sum // 2

        dp = [[-1] * (sum+1) for _ in range(n+1)]
        self.subset(n, sum, arr, dp)
        return dp[n][sum]

if __name__ == "__main__":
    sol = solution()
    arr = [1, 5, 11, 5]
    print(sol.issubsetsum(arr))
