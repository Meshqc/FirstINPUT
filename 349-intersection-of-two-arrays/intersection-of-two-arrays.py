class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for n in nums1:
            if n in nums2:
                if n not in res:
                    res.append(n)
        print(res)
        return(res)