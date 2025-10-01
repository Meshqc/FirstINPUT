class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = 0
        curr = None
        for n in nums:
            if c == 0:
                curr = n
            if n == curr:
                c += 1
            else:
                c -= 1 
        print(curr)
        return curr
            