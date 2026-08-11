class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        l=len(arr)
        freq={}
        for num in arr:
            freq[num]=freq.get(num,0)+1

        res=set()
        for num in freq:
            res.add(freq[num])
        return len(freq)==len(res)

