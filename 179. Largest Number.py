from functools import cmp_to_key

def compare(x, y):
    if x + y > y + x:
        return -1
    else:
        return 1

class Solution:
    def largest_number(self, arr):
        arr = list(map(str, arr))
        arr.sort(key=cmp_to_key(compare))
        return ''.join(arr)
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.largest_number([3, 30, 34, 5, 9]))