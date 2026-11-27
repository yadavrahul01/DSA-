# Problem: Find two numbers whose sum equals target.
# Return their indices.
#
# Example:
# nums = [2, 7, 11, 15], target = 9
# Output = [0, 1]
#
# APPROACHES:
# 1. Brute Force: Check every possible pair.
#    Time: O(n^2), Space: O(1)
#
# 2. Optimal: Use a dictionary to find the complement.
#    Time: O(n) average, Space: O(n)
#
# KEY LOGIC:
# complement = target - current_number


class Solution:
    def twoSum(self, nums, target):

        seen = {}  # Stores visited numbers and their indices

        for i in range(len(nums)):  # Traverse the array using indices

            complement = target - nums[i]  # Find the number needed to reach target

            if complement in seen:  # Check whether the required number was visited
                return [seen[complement], i]  # Return both indices

            seen[nums[i]] = i  # Store current number and its index

        # No explicit return needed because the problem guarantees one solution