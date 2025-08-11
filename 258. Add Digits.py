class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        else:
            return 1 + (num - 1) % 9

if __name__ == "__main__":
    sol = Solution()
    print(sol.addDigits(72582512))  # Output: 2