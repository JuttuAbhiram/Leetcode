class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = int(''.join(map(str, digits)))
        res=digits+1
        result=list(map(int, str(res)))
        return result