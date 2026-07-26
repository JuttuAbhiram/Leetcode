class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        largest=sec_largest=third_largest=float('-inf')
        smallest1=smallest2=float('inf')
        for i in range(len(nums)):
            if nums[i]>largest:
                third_largest=sec_largest
                sec_largest=largest
                largest=nums[i]
            elif nums[i]>sec_largest:
                third_largest=sec_largest
                sec_largest=nums[i]
            elif nums[i]>third_largest:
                third_largest=nums[i]
            
            if nums[i]<smallest1:
                smallest2=smallest1
                smallest1=nums[i]
            elif nums[i]<smallest2:
                smallest2=nums[i]
        
        return max(largest*sec_largest*third_largest,largest*smallest1*smallest2)