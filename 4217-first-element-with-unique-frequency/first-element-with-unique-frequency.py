class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1
        freqcount={}
        for f in freq.values():
            freqcount[f]=freqcount.get(f,0)+1
        for num in nums:
            if freqcount[freq[num]]==1:
                return num
        return -1