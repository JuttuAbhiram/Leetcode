class Solution:
    def arrayRankTransform(self,arr: List[int]) -> List[int]:
        unique=sorted(set(arr))
        rank={}
        for i in range(len(unique)):
            rank[unique[i]]=i+1
        
        res=[]
        for num in arr:
            res.append(rank[num])
        return res