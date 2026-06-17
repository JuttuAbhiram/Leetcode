class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        res=set()
        l=len(nums)
        ans=0
        for num in nums:
            if num in res:
                ans^=num
            else:
                res.add(num)
        return ans