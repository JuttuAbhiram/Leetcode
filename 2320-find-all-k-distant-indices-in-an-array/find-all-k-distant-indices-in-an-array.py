class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        l=len(nums)
        res=[]
        vis=[False]*l
        for i in range(l):
            if nums[i]==key:
                left=max(0,i-k)
                right=min(l-1,i+k)
                for j in range(left,right+1):
                    if not vis[j]:
                        res.append(j)
                        vis[j]=True
        
        return res