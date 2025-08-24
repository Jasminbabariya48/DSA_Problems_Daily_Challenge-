class solution:
    def solver(self, i, arr, target, subset):
        if target == 0:
            return True
            
        if i == len(arr):
            return False
            
            
        if arr[i] <= target:
            if self.solver(i+1, arr, target-arr[i], subset+[arr[i]]):
                return True
            
        if self.solver(i+1, arr, target, subset):
            return True
            
        return False


    def isSubsetSum (self, arr, sum):
        arr.sort()
        # subset = []
        
        return self.solver(0, arr, sum, [])

if __name__ == "__main__":
    arr = [3, 34, 4, 12, 5, 2]
    sum = 9
    sol = solution()
    print(sol.isSubsetSum(arr, sum))