class Solution:
    def numJewelsInStones(self, j: str, s: str) -> int:
        string = j
        dic = dict.fromkeys(string, 0)
        for char in s:
            if char in dic:
                dic[char] += 1
        print(dic)
        s = sum(dic.values())
        return s