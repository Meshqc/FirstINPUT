class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        res = None
        ran = range(len(nums)+1)
        ran = list(ran)

        for n in ran:
            if n not in nums:
                res = n
        print(res,"___",ran)
        return res
