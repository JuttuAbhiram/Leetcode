class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        n=len(arr)
        total=0
        for i in range(n):
            left=i
            right=n-i-1
            left_count=left+1
            right_count=right+1
            
            odd_left=left_count//2
            even_left=left_count-odd_left
            odd_right=right_count//2
            even_right=right_count-odd_right

            count=(odd_left*odd_right)+(even_left*even_right)
            total+=arr[i]*count
        return total