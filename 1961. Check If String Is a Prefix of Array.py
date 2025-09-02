from typing import List

class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        curr = ""
        for w in words:
            curr += w

            if curr == s:
                return True
            if len(curr) > len(s):
                return False
        return False
    
if __name__ == "__main__":
    s = Solution()
    print(s.isPrefixString("iloveleetcode", ["i", "love", "leetcode", "apples"]))  # True
    print(s.isPrefixString("iloveleetcode", ["apples", "i", "love", "leetcode"]))  # False