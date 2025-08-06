class solution:
    def solveMemo(self, word1, word2, i, j, dp):
        if i == len(word1):
            return len(word2) - j

        if j == len(word2):
            return len(word1) - i

        if dp[i][j] != -1:
            return dp[i][j]

        ans = 0
        if word1[i] == word2[j]:
            return self.solveMemo(word1, word2, i+1, j+1, dp)

        else:
            # Insert
            insert = 1 + self.solveMemo(word1, word2, i, j+1, dp)
            # Delete
            delete = 1 + self.solveMemo(word1, word2, i+1, j, dp)
            # replace
            replace = 1 + self.solveMemo(word1, word2, i+1, j+1, dp)

            ans = min(insert, min(delete, replace))
            dp[i][j] = ans
        return dp[i][j]

    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[-1 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]
        return self.solveMemo(word1, word2, 0, 0, dp)
    
if __name__ == "__main__":
    solution = solution()
    word1 = "horse"
    word2 = "ros"
    print(solution.minDistance(word1, word2))  # Output: 3