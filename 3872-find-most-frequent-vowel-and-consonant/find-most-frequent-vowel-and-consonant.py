from collections import defaultdict
class Solution:
    def maxFreqSum(self, s: str) -> int:
        vow = defaultdict(int)
        con = defaultdict(int)
        vowels = "aeiou"
        for char in s:
            if char in vowels:
                vow[char] +=1
            else:
                con[char] +=1 
        return max(vow.values(), default=0)+max(con.values(), default=0)
