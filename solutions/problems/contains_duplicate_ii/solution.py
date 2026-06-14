class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l=len(nums)
        window=set()
        for i in range(l):
            if nums[i] in window:
                return True
            window.add(nums[i])

            if len(window)>k:
                window.remove(nums[i-k])
        return False