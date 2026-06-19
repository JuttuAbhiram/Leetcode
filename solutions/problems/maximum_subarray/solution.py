class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l=len(nums)
        max_sum=nums[0]
        Sum=0
        for i in range(l):
            Sum+=nums[i]
            max_sum=max(Sum,max_sum)
            if Sum<0:
                Sum=0
        return max_sum
            
