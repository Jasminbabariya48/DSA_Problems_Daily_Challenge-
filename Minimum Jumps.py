from typing import List

class Solution:
	def minJumps(self, arr: List[int]) -> int:
	    n = len(arr)
	    dp = [n+1] * n
	    dp[0] = 0

	    for i in range(1, n):
	        for j in range(i):
	            if arr[j]+j >= i:
	                dp[i] = min(dp[i], dp[j]+1)

	    if dp[n-1] == n+1:
	        return -1

	    return dp[n-1]

if __name__ == "__main__":
	sol = Solution()
	arr = [2, 3, 1, 1, 4]
	print(sol.minJumps(arr))