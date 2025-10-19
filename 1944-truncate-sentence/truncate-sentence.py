class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        sp = s.split()
        n = 0
        res=[]
        for i in sp:
            if n != k:
                res.append(i)
                n += 1
        print(res)
        a = " ".join(res)
        return a