class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        
        while i >= 0 or j >= 0 or carry:
            sum_value = carry
            
            if i >= 0:
                sum_value += int(a[i])
                i -= 1
            if j >= 0:
                sum_value += int(b[j])
                j -= 1
            
            result.append(str(sum_value % 2))
            carry = sum_value // 2
        
        return ''.join(reversed(result))
    
if __name__ == "__main__":
    sol = Solution()
    a = "11"
    b = "1"
    print(sol.addBinary(a, b))  # Output: "100"
    a = "1010"
    b = "1011"
    print(sol.addBinary(a, b))  # Output: "10101"