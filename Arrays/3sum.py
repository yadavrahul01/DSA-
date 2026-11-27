# Problem: Find all unique triplets whose sum equals zero.
#
# Example:
# nums = [-1, 0, 1, 2, -1, -4]
# Output = [[-1, -1, 2], [-1, 0, 1]]
#
# APPROACHES:
# 1. Brute Force: Check all possible triplets.
#    Time: O(n^3), Space: O(1) auxiliary
#
# 2. Hashing: Fix one element and use a set to find pairs.
#    Time: O(n^2) average, Space: O(n)
#
# 3. Optimal: Sort and use two pointers.
#    Time: O(n^2), Space: O(1) auxiliary*
#
# KEY LOGIC:
# Sort -> Fix one number -> Find the remaining two numbers.


class Solution:
    def threeSum(self, nums):

        nums.sort()  # Sort array to use two pointers and skip duplicates

        result = []  # Store all unique triplets

        for i in range(len(nums)):  # Fix the first element of the triplet

            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicate first elements

            left = i + 1  # Second element starts after the fixed element

            right = len(nums) - 1  # Third element starts at the last position

            while left < right:  # Continue until the pointers meet

                total = nums[i] + nums[left] + nums[right]  # Calculate triplet sum

                if total < 0:
                    left += 1  # Increase sum by moving left pointer forward

                elif total > 0:
                    right -= 1  # Decrease sum by moving right pointer backward

                else:
                    # A valid triplet is found, so store it
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicate values on the left side
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Skip duplicate values on the right side
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1  # Move left pointer to search for another triplet
                    right -= 1  # Move right pointer to search for another triplet

        return result  # Return all unique triplets