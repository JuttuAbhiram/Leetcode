class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        l=len(nums)
        n=l//2
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1
        
        for num in nums:
            if freq[num]==n:
                return num