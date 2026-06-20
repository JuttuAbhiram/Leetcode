class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=len(nums)
        ind=-1
        for i in range(l-2,-1,-1):
            if nums[i]<nums[i+1]:
                ind=i
                break
        if ind==-1:
            nums.reverse()
            return
        for i in range(l-1,ind,-1):
            if nums[i]>nums[ind]:
                nums[i],nums[ind]=nums[ind],nums[i]
                break
        left=ind+1
        right=l-1
        while left<right:
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
            right-=1