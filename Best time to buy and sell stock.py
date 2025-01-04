# 1st Solution - Brute Force Approach
# This approach calculates the profit for every possible pair of buy and sell days.
# - Iterates through all possible pairs of prices.
# - Checks and updates the maximum profit for each pair.
# - Time Complexity: O(n^2), due to nested loops for every price pair.
# - Space Complexity: O(1), no additional space is used.
# - Performance: Inefficient for large input sizes.

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> List[int]:
        max_profit = 0  # Initialize the maximum profit to 0
        for i in range(len(prices)):
            buy_price = prices[i]  # Price at which to buy
            for j in range(i + 1, len(prices)):
                sell_price = prices[j]  # Price at which to sell
                profit = sell_price - buy_price  # Calculate profit
                if profit > max_profit:  # Update maximum profit if current profit is higher
                    max_profit = profit
        return max_profit  # Return the maximum profit found

# 2nd Solution - Optimized Approach
# This approach tracks the minimum price and calculates the profit in a single pass.
# - Iterates through the price list once.
# - Updates the minimum price seen so far.
# - Calculates and updates the maximum profit dynamically.
# - Time Complexity: O(n), where n is the number of prices.
# - Space Complexity: O(1), uses only a few variables for calculations.
# - Performance: Efficient, suitable for large inputs.

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> List[int]:
        max_profit = 0  # Initialize the maximum profit to 0
        min_price = float('inf')  # Start with the highest possible minimum price
        for i in prices:
            if i < min_price:  # Update minimum price if current price is lower
                min_price = i
            profit = i - min_price  # Calculate profit for the current price
            if profit > max_profit:  # Update maximum profit if current profit is higher
                max_profit = profit
        return max_profit  # Return the maximum profit found
