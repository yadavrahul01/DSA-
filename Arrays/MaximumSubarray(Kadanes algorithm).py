# Problem: Find the contiguous subarray having the maximum sum.
#
# Example:
# nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output = 6
#
# APPROACHES:
# 1. Brute Force: Generate all subarrays and calculate sums.
#    Time: O(n^3), Space: O(1)
#
# 2. Better: Use running sums to avoid repeated calculations.
#    Time: O(n^2), Space: O(1)
#
# 3. Optimal: Use Kadane's Algorithm.
#    Time: O(n), Space: O(1)
#
# KEY LOGIC:
# current_sum = max(num, current_sum + num)
# max_sum = max(max_sum, current_sum)


class Solution:
    def maxSubArray(self, nums):

        current_sum = nums[0]  # Maximum subarray sum ending at first element

        max_sum = nums[0]  # Initialize overall maximum sum with first element

        for num in nums[1:]:  # Traverse the remaining elements

            # Choose between starting a new subarray or extending the previous one
            current_sum = max(num, current_sum + num)

            # Update the overall maximum subarray sum
            max_sum = max(max_sum, current_sum)

        return max_sum  # Return the largest contiguous subarray sum