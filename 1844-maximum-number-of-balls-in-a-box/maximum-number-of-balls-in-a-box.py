class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        freq={}
        for num in range(lowLimit,highLimit+1):
            temp=num
            Sum=0
            while temp>0:
                last_digit=temp%10
                Sum+=last_digit
                temp=temp//10
            freq[Sum]=freq.get(Sum,0)+1
        return max(freq.values())
