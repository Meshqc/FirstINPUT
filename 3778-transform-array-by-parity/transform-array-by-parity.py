class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        r = []
        for n in range(len(nums)):
            if nums[n] % 2 != 0:
                r.append(1)
            elif nums[n] % 2 == 0:
                r.append(0)
        res = sorted(r)
        print(res)
        return(res)
        
        