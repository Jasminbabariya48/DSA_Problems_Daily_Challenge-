from typing import List

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 0 or arr[0] == 0:
            return -1

        jumps = 0
        curr_end = 0
        curr_farthest = 0

        for i in range(n - 1):
            curr_farthest = max(curr_farthest, i + arr[i])
            if i == curr_end:
                jumps += 1
                curr_end = curr_farthest
                if curr_end >= n - 1:
                    break

        return jumps if curr_end >= n - 1 else -1

if __name__ == "__main__":
    sol = Solution()
    arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
    print(sol.minJumps(arr))