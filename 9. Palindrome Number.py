class solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        reversed_num = 0
        original_num = x
        while x > 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10
        return original_num == reversed_num
    
if __name__ == "__main__":
    sol = solution()
    print(sol.isPalindrome(121))  # True
    print(sol.isPalindrome(-121))  # False
    print(sol.isPalindrome(10))    # False