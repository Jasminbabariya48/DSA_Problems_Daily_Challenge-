from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        st = set(wordDict)
        n = len(s)

        dp = [[] for _ in range(n+1)]
        dp[n].append('')

        for i in range(n-1, -1, -1):
            for j in range(i+1,n+1):
                word = s[i:j]
                
                if word in st:
                    for sub in dp[j]:
                        if sub:
                            dp[i].append(word + " " + sub)
                            
                        else:
                            dp[i].append(word)
        return dp[0]
    
if __name__ == "__main__":
    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    solution = Solution()
    print(solution.wordBreak(s, wordDict))