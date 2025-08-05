class Solution:
    def countSubstrings(self, s: str) -> int:
        def count_pali(left, right):
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 >= 1:
                    count += 1
                left -= 1
                right += 1
            return count
            
        n = len(s)
        res = 0
        for c in range(n):
            res += count_pali(c, c)
            res += count_pali(c, c+1)
                
        return res
    
if __name__ == "__main__":
    solution = Solution()
    s = "abc"
    print(solution.countSubstrings(s))  # Output: 3