class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        l=len(nums)
        a=min(nums)
        b=max(nums)
        num=set(nums)
        res=[]
        for i in range(a,b):
            if i not in num:
                res.append(i)
        return res


