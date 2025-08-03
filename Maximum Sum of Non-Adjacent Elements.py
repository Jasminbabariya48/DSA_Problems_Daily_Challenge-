class solution:
    def maxsumNonAdjacent(self, nums: list[int]) -> int:
        # DP IN Tabulation
        n = len(nums)
        if n == 0:
            return 0
        
        if n == 1:
            return nums[0]

        dp = [0] * n

        dp[0] = nums[0]

        for i in range(1, n):                    # right to left
            include = dp[i-2] + nums[i]
            exclude = dp[i-1] + 0

            dp[i] = max(include, exclude)
        return dp[n-1]
    
if __name__ == "__main__":
    solution = solution()
    nums = [3, 2, 5, 10, 7]
    print(solution.maxsumNonAdjacent(nums))  # Output: 15