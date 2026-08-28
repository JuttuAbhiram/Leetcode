class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        for i,value in enumerate(nums):
            if i%10==value:
                return i
        return -1