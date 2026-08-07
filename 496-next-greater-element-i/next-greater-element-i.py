class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        mapp={}
        for num in nums2:
            while stack and num>stack[-1]:
                mapp[stack.pop()]=num
            stack.append(num)
        while stack:
            mapp[stack.pop()]=-1
        ans=[]
        for num in nums1:
            ans.append(mapp[num])
        
        return ans
            