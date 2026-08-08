class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1
        Sum=0
        for num in freq:
            if freq[num]==1:
                Sum+=num
        return Sum
        