from typing import List

class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        n = len(reward1)
        total = sum(reward2)
        
        diffs = [reward1[i] - reward2[i] for i in range(n)]
        
        diffs.sort(reverse=True)
        total += sum(diffs[:k])
        
        return total
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.miceAndCheese([1,1,3,4], [4,4,1,1], 2))  # Output: 15
    print(solution.miceAndCheese([1,1], [1,1], 2))          # Output: 2
        