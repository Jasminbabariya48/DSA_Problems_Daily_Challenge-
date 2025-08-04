class solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] =True
        
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                
        for l in range(3, n+1):
            for i in range(n-l+1):
                if s[i] == s[i+l-1] and dp[i+1][i+l-2] == True:
                    dp[i][i+l-1] = True
                
        start = 0
        maxlen = 1
        
        for i in range(n):
            for j in range(i, n):
                if dp[i][j] == True:
                    if (j-i+1) > maxlen:
                        maxlen = j-i+1
                        start = i
        return s[start:start+maxlen]
    
if __name__ == "__main__":
    solution = solution()
    s = "babad"
    print(solution.longestPalindrome(s))  # Output: "bab" or "aba"