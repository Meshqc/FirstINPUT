class Solution:
    def stableMountains(self, h: List[int], t: int) -> List[int]:
        res = []
        n = len(h)
        for i in range(n)[1:]:
            if h[i-1] > t:
                res.append(i)
        print(res)
        return res