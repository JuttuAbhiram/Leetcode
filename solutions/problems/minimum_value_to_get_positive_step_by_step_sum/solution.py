class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        l=len(nums)
        result=[]
        sum1=0
        min_prefix=0
        for i in nums:
            sum1=sum1+i
            result.append(sum1)
        s=min(result)
        return 1-min(s,min_prefix)