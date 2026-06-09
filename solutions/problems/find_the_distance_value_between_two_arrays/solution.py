class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        count = 0 
        for x in arr1: 
            pos = bisect_left(arr2, x) 
            valid = True 
            if pos < len(arr2) and abs(arr2[pos] - x) <= d:
                 valid = False 
            if pos > 0 and abs(arr2[pos - 1] - x) <= d:
                 valid = False 
            if valid: 
                count += 1 
        return count

        