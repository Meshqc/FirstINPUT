class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        eve = []
        res = []
        for i in range(len(nums)):
            eve.append(len(str(nums[i])))
        print(eve)
        for n in eve:
            if n %2==0:
                res.append(n)
        return len(res)
