class solution:
    def truncateSentence(self, s: str, k: int) -> str:
        words = s.split()
        return ' '.join(words[:k])
    
if __name__ == "__main__":
    sol = solution()
    print(sol.truncateSentence("Hello how are you Contestant", 4))