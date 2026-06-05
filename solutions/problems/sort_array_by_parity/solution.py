class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even_res=[]
        odd_res=[]
        for num in nums:
            if num%2==0:
                even_res.append(num)
            else:
                odd_res.append(num)
        return even_res+odd_res