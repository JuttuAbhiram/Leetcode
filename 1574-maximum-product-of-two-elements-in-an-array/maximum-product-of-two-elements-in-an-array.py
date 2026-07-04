class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        largest=0
        secondLargest=0
        for num in nums:
            if num>largest:
                secondLargest=largest
                largest=num
            elif num>secondLargest:
                secondLargest=num
        return (largest-1)*(secondLargest-1)