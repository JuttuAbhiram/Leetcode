class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res=[]
        maxi=max(candies)
        for candie in candies:
            if candie+extraCandies>=maxi:
                res.append(True)
            else:
                res.append(False)
        return res