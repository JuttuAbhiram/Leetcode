class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos_index=0
        neg_index=1
        l=len(nums)
        num=[0]*l
        for i in range(l):
            if nums[i]>0:
                num[pos_index]=nums[i]
                pos_index+=2
            else:
                num[neg_index]=nums[i]
                neg_index+=2
            
        return num