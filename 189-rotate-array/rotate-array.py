class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        l=len(nums)
        k=k%l
        nums.reverse()
        nums[:k]=reversed(nums[:k])
        nums[k:]=reversed(nums[k:])

