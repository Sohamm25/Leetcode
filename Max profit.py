from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        abc = 0
        for i in prices:
            for j in range(prices.index(i) + 1, len(prices) - 1):
                a = i - prices[j]
                if a < 1:
                    a * (-1)
                if a > max(abc):
                    abc.append(a)