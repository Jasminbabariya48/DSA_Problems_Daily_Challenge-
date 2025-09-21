from typing import List

class Solution:
    def maxHistogramArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        n = len(heights)
        
        for i in range(n + 1):
            h = heights[i] if i < n else 0
            while stack and h < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
        
        return max_area
    
    def maxArea(self, mat: List[List[int]]) -> int:
        if not mat or not mat[0]:
            return 0
        
        n, m = len(mat), len(mat[0])
        heights = [0] * m
        max_area = 0
        
        for i in range(n):
            for j in range(m):
                heights[j] = heights[j] + 1 if mat[i][j] == 1 else 0
            max_area = max(max_area, self.maxHistogramArea(heights))
        
        return max_area
            
if __name__ == "__main__":
    sol = Solution()
    matrix = [
        [0, 1, 1, 0],
        [1, 1, 1, 1],
        [1, 1, 1, 0],
        [1, 1, 0, 0]
    ]
    print(sol.maxArea(matrix))  # Output: 8
    matrix = [
        [0, 0, 0],
        [0, 0, 0]
    ]
    print(sol.maxArea(matrix))  # Output: 0
    matrix = [
        [1, 1, 1],
        [1, 1, 1]
    ]
    print(sol.maxArea(matrix))  # Output: 6
    matrix = [
        [1]
    ]
    print(sol.maxArea(matrix))  # Output: 1
        
        
        