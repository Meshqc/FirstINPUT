class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        op = 0 
        for n in nums:
            if n % 3 != 0:
                op += 1
        return op