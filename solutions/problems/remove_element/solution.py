class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        s=0
        n=len(nums)
        for num in range(n):
            if nums[num]!=val:
                nums[s]=nums[num]
                s+=1
        return s