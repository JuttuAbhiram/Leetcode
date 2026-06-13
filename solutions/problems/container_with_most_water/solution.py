class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=len(height)
        right=l-1
        left=0
        max_capacity=0
        while left<right:
            s=min(height[left],height[right])
            width=right-left
            area=s*width
            max_capacity=max(area,max_capacity)
            if height[left]>height[right]:
                right-=1
            else:
                left+=1
        return max_capacity

