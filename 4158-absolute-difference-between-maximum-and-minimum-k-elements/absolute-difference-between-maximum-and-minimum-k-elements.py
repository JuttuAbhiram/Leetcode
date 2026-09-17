class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        l=len(nums)
        nums.sort()
        sum1=sum(nums[:k])
        sum2=sum(nums[-k:])
        return abs(sum1-sum2)