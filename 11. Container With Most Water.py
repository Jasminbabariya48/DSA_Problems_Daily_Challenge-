class Solution:
    def maxWater(self, arr):
        left = 0
        right = len(arr) - 1
        
        max_area = 0
        
        while left < right:
            hight = min(arr[left], arr[right])
            width = right - left
            
            area = hight * width
            
            max_area = max(max_area, area)
            
            if arr[left]  < arr[right]:
                left += 1
                
            else:
                right -= 1
                
        return max_area
                
if __name__ == "__main__":
    solution = Solution()
    arr = [1,8,6,2,5,4,8,3,7]
    print(solution.maxWater(arr))