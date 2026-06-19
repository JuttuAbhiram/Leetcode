class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=len(prices)
        max_profit=0
        diff=prices[0]
        for i in range(l):
            profit=prices[i]-diff
            max_profit=max(max_profit,profit)
            diff=min(diff,prices[i])
        return max_profit