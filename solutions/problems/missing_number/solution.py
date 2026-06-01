class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l=len(nums)
        sum1=0
        for i in nums:
            sum1=sum1+i
        n=l*(l+1)//2
        return n-sum1 