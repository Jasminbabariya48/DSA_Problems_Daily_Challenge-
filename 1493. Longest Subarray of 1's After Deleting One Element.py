class Solution:
    def longestSubarray(self, nums) -> int:
        left = 0
        max_length = 0
        last_zero = -1

        for right in range(len(nums)):
            if nums[right] == 0:
                left = last_zero + 1
                last_zero = right
            
            max_length = max(max_length, right - left)
        
        return max_length
        
if __name__ == "__main__":
    sol = Solution()
    print(sol.longestSubarray([1, 1, 0, 1]))  # Output: 3
    print(sol.longestSubarray([0, 1, 1, 0, 1]))  # Output: 4
    print(sol.longestSubarray([1, 1, 1]))  # Output: 2
    print(sol.longestSubarray([0, 0, 0]))  # Output: 0
