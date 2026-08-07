class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freq={}
        for num in arr1:
            freq[num]=freq.get(num,0)+1
        ans=[]
        for num in arr2:
            while freq[num]>0:
                ans.append(num)
                freq[num]-=1
        remain=[]
        for num in freq:
            while freq[num]>0:
                remain.append(num)
                freq[num]-=1
        remain.sort()
        return ans+remain