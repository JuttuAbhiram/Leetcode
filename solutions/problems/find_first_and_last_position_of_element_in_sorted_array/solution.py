class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        s=[]
        for i in range(len(nums)):
            if target==nums[i]:
                s.append(i)
        if s:
            return [s[0], s[-1]]
        else:
            return [-1,-1]
            
        