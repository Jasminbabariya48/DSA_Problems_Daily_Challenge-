from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        # Find the minimum length string in the list
        min_str = min(strs, key=len)
        # Check each character of the minimum string
        for i in range(len(min_str)):
            for s in strs:
                if s[i] != min_str[i]:
                    return min_str[:i]
        return min_str
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.longestCommonPrefix(["flower", "flow", "flight"]))
    print(solution.longestCommonPrefix(["dog", "racecar", "car"]))  