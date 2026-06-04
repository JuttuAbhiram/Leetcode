class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected=sorted(heights)
        l=len(heights)
        count=0
        for i in range(l):
            if heights[i]!=expected[i]:
                count=count+1
        return count