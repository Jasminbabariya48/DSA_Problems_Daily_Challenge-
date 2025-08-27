class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = " ".join(s.split())

        words = s.split()

        res = []
        for w in words:
            res.append(len(w))
        return res[-1] if res else 0
    
if __name__ == "__main__":
    solution = Solution()
    test_string = "   fly me   to   the moon  "
    print(solution.lengthOfLastWord(test_string))  # Output: 4
