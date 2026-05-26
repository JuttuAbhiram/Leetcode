class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n=len(nums)
        result=[]
        sum=0
        for i in range(n):
            sum=sum+nums[i]
            result.append(sum)
        return result        