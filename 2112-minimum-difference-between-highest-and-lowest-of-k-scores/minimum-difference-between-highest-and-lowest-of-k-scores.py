class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        l=len(nums)
        nums.sort()
        min_diff=float("inf")
        for i in range(l-k+1):
            diff=nums[i+k-1]-nums[i]
            if diff<min_diff:
                min_diff=diff
        return min_diff