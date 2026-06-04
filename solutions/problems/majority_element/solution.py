class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num=sorted(nums)
        l=len(num)
        res=l//2
        return num[res]