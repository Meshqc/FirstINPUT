import math
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        maxx = max(nums)
        minn = min(nums)
        div = math.gcd(maxx,minn)
        print(div)
        return div

        