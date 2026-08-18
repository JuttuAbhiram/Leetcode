class Solution:
    def calPoints(self, operations: List[str]) -> int:
        l=len(operations)
        res=[]
        for op in operations:
            if op.lstrip('-').isdigit():
                res.append(int(op))
            elif op=='C':
                res.remove(res[-1])
            elif op=='D':
                res.append(res[-1]*2)
            elif op=='+':
                res.append(res[-1]+res[-2])
        return sum(res)