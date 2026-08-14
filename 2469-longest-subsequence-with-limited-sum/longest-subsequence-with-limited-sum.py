class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefix=[]
        total=0
        for num in nums:
            total+=num
            prefix.append(total)
        
        res=[]
        for query in queries:
            count=0
            for value in prefix:
                if value<=query:
                    count+=1
                else:
                    break
            res.append(count)
        
        return res