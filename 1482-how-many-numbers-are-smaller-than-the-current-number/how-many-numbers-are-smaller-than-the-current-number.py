class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        l=len(nums)
        res=[]
        for i in range(l):
            left=0
            count=0
            while left<=l-1:
                if nums[i]>nums[left]:
                    count+=1
                left+=1
            res.append(count)
        return res