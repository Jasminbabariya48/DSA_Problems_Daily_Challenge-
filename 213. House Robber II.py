from typing import List

class Solution:
    def solver(self, arr): # pyright: ignore[reportUnknownParameterType]
        n = len(arr)
        if n < 0:
            return 0
        if n == 1:
            return arr[0]

        dp = [0] * n
        dp[0] = arr[0]
        dp[1] = max(arr[0], arr[1])

        for i in range(2, n-1):
            dp[i] = max(dp[i-1], dp[i-2] + arr[i])

        return dp[n-1]

    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        first = []
        second = []
        for i in range(n):
            if i != n - 1:
                first.append(nums[i])
            if i != 0:
                second.append(nums[i])
        return max(self.solver(first), self.solver(second))
    
if __name__ == "__main__":
    solution = Solution()   
    nums = [2,3,2]
    print(solution.rob(nums))  # Output: 3

