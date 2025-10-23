class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        result = [num for num, count in counts.items() if count == 2]
        return result