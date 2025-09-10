class Solution:
    def largestSwap(self, s):
        l = list(s)
        n = len(s)
        
        for i in range(n):
            max_index = i
            for j in range(i+1, n):
                if l[j] >= l[max_index]:
                    max_index = j
            if l[max_index] > l[i]:
                l[i], l[max_index] = l[max_index], l[i]
                
                ans = ""
                for i in l:
                    ans += i
                return ans
        return s
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.largestSwap("2736"))  # Output: "7236"
    print(solution.largestSwap("9973"))  # Output: "9973"