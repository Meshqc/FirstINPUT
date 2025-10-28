class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        res = []
        for n in nums:
            if n < k:
                res.append(n)
        print(res)
        return len(res)