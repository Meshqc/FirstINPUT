class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        position = 0
        for n in nums:
            if n != 0:
                nums[position] = n
                position += 1
        print(nums)
        while position < len(nums):
            nums[position] = 0
            position += 1

 
        