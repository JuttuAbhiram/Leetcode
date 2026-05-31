class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        m_wealth=0

        for i in accounts:
            wealth=sum(i)

            if wealth>m_wealth:
                m_wealth=wealth
        return m_wealth