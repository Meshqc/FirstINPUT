class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        r = []
        for e in nums:
            if e%2==0:
                e = 0
            else: 
                e = 1
            r.append(e)
        r.sort()
        return r

        
        