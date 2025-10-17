class Solution:
    def finalValueAfterOperations(self, op: List[str]) -> int:
        res = 0
        for i in op:
            if "+" in i:
                res +=1
            if "-" in i:
                res -=1
        print(res)
        return(res)
