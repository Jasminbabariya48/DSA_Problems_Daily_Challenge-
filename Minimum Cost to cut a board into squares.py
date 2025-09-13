class Solution:
    def minCost(self, n, m, x, y):
        # Sort descending
        x.sort(reverse=True)
        y.sort(reverse=True)
    
        i, j = 0, 0
        hz_segments, vt_segments = 1, 1
        cost = 0
    
        # Process both lists
        while i < len(x) and j < len(y):
            if x[i] > y[j]:  # vertical cut
                cost += x[i] * hz_segments
                vt_segments += 1
                i += 1
            else:            # horizontal cut
                cost += y[j] * vt_segments
                hz_segments += 1
                j += 1
    
        # Remaining vertical cuts
        while i < len(x):
            cost += x[i] * hz_segments
            vt_segments += 1
            i += 1
    
        # Remaining horizontal cuts
        while j < len(y):
            cost += y[j] * vt_segments
            hz_segments += 1
            j += 1
    
        return cost
        
        
if __name__ == "__main__":
    solution = Solution()
    n = 6
    m = 4
    x = [2, 1, 3, 1, 4]  # vertical cuts
    y = [4, 1, 2]        # horizontal cuts
    print(solution.minCost(n, m, x, y))  # Output: 42