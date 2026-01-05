class Solution:
    def maxFreqSum(self, s: str) -> int:
        vow = {}
        con = {}
        vowels = "aeiou"
        for char in s:
            if char in vowels:
                if char in vow:
                    vow[char] +=1
                else:
                    vow[char] = 1
            else:
                if char in con:
                    con[char] +=1
                else:
                    con[char] = 1
        print(vow)
        print(con)
        return max(vow.values(), default=0)+max(con.values(), default=0)
