class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        freq={}
        for num in s:
            freq[num]=freq.get(num,0)+1
        values=list(freq.values())
        if len(set(values))==1:
            return True
        else:
            return False