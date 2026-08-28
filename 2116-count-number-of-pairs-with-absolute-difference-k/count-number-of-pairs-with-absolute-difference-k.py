class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        i=0
        count=0
        while i<=len(nums)-1:
            for j in range(i+1,len(nums)):
                if abs(nums[i]-nums[j])==k:
                    count+=1
            i+=1
        return count
