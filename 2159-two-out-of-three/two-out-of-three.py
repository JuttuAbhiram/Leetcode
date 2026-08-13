class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        s1=set(nums1)
        s2=set(nums2)
        s3=set(nums3)
        result=set()

        result.update(s1 & s2)
        result.update(s2 & s3)
        result.update(s1 & s3)

        return list(result)