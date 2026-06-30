class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l=len(nums)
        low=0
        high=l-1
        ans=l
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>=target:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
