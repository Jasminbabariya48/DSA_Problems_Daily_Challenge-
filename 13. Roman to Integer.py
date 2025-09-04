from typing import List

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0
        n = len(s)
        
        for i in range(n):
            if i+1 < n and roman_numerals[s[i]] < roman_numerals[s[i+1]]:
                total -= roman_numerals[s[i]]
                
            else:
                total += roman_numerals[s[i]]

        return total
    
if __name__ == "__main__":
    solution = Solution()
    roman_string = "MCMXCIV"
    result = solution.romanToInt(roman_string)
    print(f"The integer value of the Roman numeral {roman_string} is {result}.")
        