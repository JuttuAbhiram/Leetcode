class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=len(nums)
        left=0
        total_sum=0
        min_len=float("inf")
        for i in range(l):
            total_sum+=nums[i]
            while total_sum>=target:
                min_len=min(i-left+1,min_len)
                total_sum-=nums[left]
                left+=1
        if min_len==float("inf"):
            return 0
        else:
            return min_len
        
