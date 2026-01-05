class Solution:
    def numJewelsInStones(self, j: str, s: str) -> int:
        j = set(j)
        count = 0 
        for char in s:
            if char in j:
                count += 1
        return count