class Solution:
    def reverseDegree(self, s: str) -> int:
        total=0
        for i in range(len(s)):
            ch=s[i]
            reverse=122-ord(ch)+1
            total+=reverse*(i+1)
        return total
