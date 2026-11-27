# Problem: Every element appears twice except one element.
# Find the element that appears only once.
#
# Example:
# nums = [4, 1, 2, 1, 2]
# Output = 4
#
# APPROACHES:
# 1. Brute Force: Count occurrences of every element.
#    Time: O(n^2) using repeated counting, Space: O(1)
#
# 2. Hashing: Store element frequencies in a dictionary.
#    Time: O(n) average, Space: O(n)
#
# 3. Optimal: Use XOR bit manipulation.
#    Time: O(n), Space: O(1)
#
# PATTERN: Bit Manipulation + XOR
#
# KEY XOR PROPERTIES:
# a ^ a = 0
# a ^ 0 = a
# XOR is commutative and associative.
#
# Therefore, duplicate numbers cancel each other out.


class Solution:
    def singleNumber(self, nums):

        result = 0  # Initialize XOR result with zero

        for num in nums:  # Traverse every number in the array

            result ^= num  # XOR current number with the result

            # Duplicate numbers cancel because a ^ a = 0

        return result  # Only the number appearing once remains