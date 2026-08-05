class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        r = []
        for e in nums:
            if e%2==0:
                r.append(0)
            else: 
                r.append(1)
        r.sort()
        return r

        
        