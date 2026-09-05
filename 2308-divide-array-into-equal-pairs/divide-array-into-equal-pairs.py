class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        l=len(nums)
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1
        for values in freq.values():
            if values%2!=0:
                return False
        return True