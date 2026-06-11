class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left_sum=0
        total_sum=sum(nums)
        res=[]
        for num in range(len(nums)):
            right_sum=total_sum-left_sum-nums[num]
            s=abs(left_sum-right_sum)
            res.append(s)
            left_sum=left_sum+nums[num]
        return res
        