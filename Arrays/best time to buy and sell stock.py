# Problem: Find the maximum profit by buying a stock on one day
# and selling it on a future day.
#
# Example:
# prices = [7, 1, 5, 3, 6, 4]
# Output = 5
#
# Explanation:
# Buy at 1 and sell at 6.
# Profit = 6 - 1 = 5
#
# APPROACHES:
# 1. Brute Force: Check every possible buying and selling pair.
#    Time: O(n^2), Space: O(1)
#
# 2. Optimal: Track minimum buying price and maximum profit.
#    Time: O(n), Space: O(1)
#
# PATTERN: Greedy + One Pass
#
# KEY LOGIC:
# profit = current_price - minimum_price
# Update minimum price whenever a cheaper price is found.


class Solution:
    def maxProfit(self, prices):

        min_price = float('inf')  # Initialize minimum buying price as infinity

        max_profit = 0  # Store the maximum profit found so far

        for price in prices:  # Traverse each day's stock price

            if price < min_price:
                min_price = price  # Update the cheapest buying price

            else:
                profit = price - min_price  # Calculate profit if sold today

                max_profit = max(max_profit, profit)  # Keep the highest profit

        return max_profit  # Return maximum profit (0 if no profit is possible)