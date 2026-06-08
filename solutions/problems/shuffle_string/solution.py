class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        l=len(s)
        res=[""]*l

        for i in range(l):
            res[indices[i]]=s[i]

        return "".join(res)
        