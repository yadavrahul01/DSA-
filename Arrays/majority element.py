# Problem: Find the element that appears more than n//2 times.
#
# Example:
# nums = [2, 2, 1, 1, 1, 2, 2]
# Output = 2
#
# APPROACHES:
# 1. Brute Force: Count occurrences of each element.
#    Time: O(n^2), Space: O(1)
#
# 2. Hashing: Store frequency of each element in a dictionary.
#    Time: O(n) average, Space: O(n)
#
# 3. Optimal: Use Boyer-Moore Voting Algorithm.
#    Time: O(n), Space: O(1)
#
# PATTERN: Greedy + Boyer-Moore Voting
#
# KEY LOGIC:
# If count becomes zero, select the current number as candidate.
# If current number matches candidate, increase count.
# Otherwise, decrease count.
#
# NOTE:
# LeetCode guarantees that a majority element exists.


class Solution:
    def majorityElement(self, nums):

        candidate = None  # Store the current majority candidate

        count = 0  # Track the candidate's voting balance

        for num in nums:  # Traverse every element in the array

            if count == 0:
                candidate = num  # Choose a new candidate when balance is zero

            if num == candidate:
                count += 1  # Increase votes for the current candidate

            else:
                count -= 1  # Decrease votes when another number appears

        return candidate  # Return the majority element