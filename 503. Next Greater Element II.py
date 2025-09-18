from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = []

        for i in range(2 * n - 1, -1, -1):
            while stack and stack[-1] <= nums[i % n]:
                stack.pop()
            if i < n:
                if stack:
                    res[i] = stack[-1]
            stack.append(nums[i % n])

        return res
    
if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 1]
    print(sol.nextGreaterElements(nums))
    # Output: [2, -1, 2]
