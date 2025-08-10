class Solution:
    def canThreePartsEqualSum(self, arr):
        res = []
        total = 0
        
        for el in arr:
            total += el
            
        if total % 3 != 0:
            res = [-1, -1]
            return False
            
        cursum = 0
        
        for i in range(len(arr)):
            cursum += arr[i]
            
            if cursum == total / 3:
                cursum = 0
                res.append(i)
                
            if len(res) == 2 and i < len(arr) - 1:
                return True
                
        res = [-1,-1]
        return False
        
if __name__ == "__main__":
    sol = Solution()
    print(sol.canThreePartsEqualSum([0, 2, 1, -6, 6, -7, 9, 1, -2, 0, 1]))  # True
    print(sol.canThreePartsEqualSum([0, 2, 1, -6, 6, -7, 9, 1, -2, 0]))  # False
    print(sol.canThreePartsEqualSum([1, -1, 1, -1]))  # True