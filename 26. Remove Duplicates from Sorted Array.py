from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1

        for j in range(1, len(nums)):
            if nums[j] != nums[i - 1]:
                nums[i] = nums[j]
                i += 1
        
        return i
    
if __name__ == "__main__":
    sol = Solution()
    nums = [1, 1, 2]
    new_length = sol.removeDuplicates(nums)
    print("New length:", new_length)
    print("Modified array:", nums[:new_length])