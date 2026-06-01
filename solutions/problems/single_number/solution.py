class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res=0
        n=len(nums)
        for j in nums:
                res^=j
        return res
        