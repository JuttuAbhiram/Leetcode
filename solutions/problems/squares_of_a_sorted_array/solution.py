class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l=len(nums)
        left=0
        right=l-1
        res=[0]*l
        pos=l-1
        while left<=right:
            if abs(nums[right])>abs(nums[left]):
                res[pos]=nums[right]**2
                right-=1
            else:
                res[pos]=nums[left]**2
                left+=1
            pos-=1
        return res


