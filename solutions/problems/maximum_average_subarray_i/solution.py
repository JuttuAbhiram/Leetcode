class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l=len(nums)
        k_sum=sum(nums[:k])
        best=k_sum
        for i in range(k,l):
            k_sum+=nums[i]-nums[i-k]
            best=max(k_sum,best)
        return best/k