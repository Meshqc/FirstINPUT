class Solution:
    def maximumWealth(self, ac: List[List[int]]) -> int:
        res = []
        for i in ac:
            res.append(sum(i))
        return max(res)

            