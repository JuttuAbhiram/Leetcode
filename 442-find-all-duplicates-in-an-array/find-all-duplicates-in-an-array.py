class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1
        res=[]
        for num in freq:
            if freq[num]==2:
                res.append(num)
        return res
