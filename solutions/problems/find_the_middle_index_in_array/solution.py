class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        left_sum=0
        total_sum=sum(nums)
        for num in range(len(nums)):
            right_sum=total_sum-left_sum-nums[num]

            if left_sum==right_sum:
                return num
            left_sum+=nums[num]
        return -1
        
