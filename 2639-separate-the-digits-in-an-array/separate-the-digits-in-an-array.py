class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res=[]
        for num in nums:
            res.extend(int(digit) for digit in str(num))
        return res