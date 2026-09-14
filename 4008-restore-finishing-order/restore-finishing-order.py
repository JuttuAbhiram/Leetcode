class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        friends_set=set(friends)
        res=[]
        for num in order:
            if num in friends_set:
                res.append(num)
        
        return res