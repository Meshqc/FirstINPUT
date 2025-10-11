class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        k = 0
        ln = len(nums)
        for i in range(ln):
            for n in range(i+1,ln):
                if nums[i] == nums[n]:
                    k += 1
        print(k)
        return k