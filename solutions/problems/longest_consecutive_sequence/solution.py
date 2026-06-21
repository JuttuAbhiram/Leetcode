class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset=set(nums)
        max_len=0
        for num in hashset:
            if num-1 not in hashset:
                nxt=num
                lnth=1
                while nxt+1 in hashset:
                    nxt+=1
                    lnth+=1
                max_len=max(max_len,lnth)
        return max_len