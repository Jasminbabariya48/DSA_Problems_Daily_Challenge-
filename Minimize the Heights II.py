class Solution:
    def minimizeTheHeights(self, arr, n, k):
        if not arr:
            return 0
        arr.sort()
        n = len(arr)
        
        if n == 1:
            return 0
        
        ans = arr[-1] - arr[0]
        
        smallest = arr[0] + k
        largest = arr[-1] - k
        
        for i in range(n-1):
            minn = min(smallest, arr[i+1] - k)
            maxx = max(largest, arr[i] + k)
            
            if minn < 0:
                continue
            
            ans = min(ans, maxx-minn)
            
        return ans
    
if __name__ == "__main__":
    solution = Solution()
    arr = [1, 5, 8, 10]
    k = 2
    n = len(arr)
    print(solution.minimizeTheHeights(arr, n, k))  # Output: 5