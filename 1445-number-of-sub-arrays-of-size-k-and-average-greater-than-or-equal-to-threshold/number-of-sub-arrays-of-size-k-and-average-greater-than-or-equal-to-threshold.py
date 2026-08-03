class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l=len(arr)
        left=0
        Sum=0
        count=0
        target=threshold*k
        for right in range(l):
            Sum+=arr[right]
            if right-left+1>k:
                Sum-=arr[left]
                left+=1
            
            if right-left+1==k:
                if Sum>=target:
                    count+=1
        return count

    