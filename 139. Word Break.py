from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for w in wordDict:
                start = i - len(w)
                if start >= 0 and dp[start] and s[start:start + len(w)] == w:
                    dp[i] = True
                    break

        return True if dp[len(s)] else False
    
if __name__ == "__main__":
    s = "leetcode"
    wordDict = ["leet", "code"]
    solution = Solution()
    print(solution.wordBreak(s, wordDict))