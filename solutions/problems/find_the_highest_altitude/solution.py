class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude=[0]
        sum1=0
        for num in gain:
            sum1=sum1+num
            altitude.append(sum1)
        return max(altitude)