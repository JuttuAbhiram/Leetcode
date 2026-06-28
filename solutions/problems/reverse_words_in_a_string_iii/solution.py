class Solution:
    def reverseWords(self, s: str) -> str:
        st=s.split()
        res=[]
        for word in st:
            res.append("".join(reversed(word)))

        return " ".join(res)

