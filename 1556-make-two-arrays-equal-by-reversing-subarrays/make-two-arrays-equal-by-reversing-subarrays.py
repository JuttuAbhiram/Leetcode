class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:

        target_freq={}
        for num in target:
            target_freq[num]=target_freq.get(num,0)+1
        
        arr_freq={}
        for num in arr:
            arr_freq[num]=arr_freq.get(num,0)+1

        return arr_freq==target_freq
            