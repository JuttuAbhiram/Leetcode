class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        remove=len(arr)//20
        remain=arr[remove:len(arr)-remove]
        return sum(remain)/len(remain)