class Solution:
    def hammingWeight(self, n: int) -> int:
        binary=bin(n)[2:]
        lst=list(map(int,binary))
        count=0
        for num in lst:
            if num==1:
                count+=1
        return count
 
            