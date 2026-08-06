class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            product=1
            for digit in str(n):
                product*=int(digit)
                
            if product%t==0:
                return n
            else:
                n+=1    

