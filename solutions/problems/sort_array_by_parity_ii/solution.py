class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        l=len(nums)
        res=[0]*l
        even_index=0
        odd_index=1
        for num in nums:
            if num%2==0:
                res[even_index]=num
                even_index+=2
            else:
                res[odd_index]=num
                odd_index+=2
        return res
