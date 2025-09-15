class Solution:
    def stringStack(self, pat, tar):
        i = len(pat)-1
        j = len(tar)-1
        
        skip = 0
        while i >= 0:
            if skip > 0:
                skip -= 1
                i -= 1
            elif j >= 0 and pat[i] == tar[j]:
                j -= 1
                i -= 1
            else:
                # use this pat[i] as a delete operation (it will remove one previously appended char)
                skip += 1
                i -= 1
        return j < 0
    
if __name__ == "__main__":
    solution = Solution() # type: ignore
    pat = "ab#c"
    tar = "ad#bc"
    print(solution.stringStack(pat, tar))  # type: ignore # Output: True
                
        