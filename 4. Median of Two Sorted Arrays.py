from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Merge the two sorted arrays
        merged = sorted(nums1 + nums2)
        n = len(merged)
        # Find the median
        if n % 2 == 1:
            return merged[n // 2]
        else:
            return (merged[n // 2 - 1] + merged[n // 2]) / 2
        

if __name__ == "__main__":
    sol = Solution()
    print(sol.findMedianSortedArrays([1, 3], [2]))  # Output: 2.0
    print(sol.findMedianSortedArrays([1, 2], [3, 4]))  # Output: 2.5