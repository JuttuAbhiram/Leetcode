class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        total_sum=0
        while n:
            last_digit=n%10
            total_sum+=last_digit
            n=n//10
            
        return total_sum


 