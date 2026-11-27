# Problem: Find all unique quadruplets whose sum equals target.
#
# Example:
# nums = [1, 0, -1, 0, -2, 2], target = 0
# Output = [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
#
# APPROACHES:
# 1. Brute Force: Check all possible quadruplets.
#    Time: O(n^4), Space: O(1) auxiliary
#
# 2. Hashing: Fix two elements and search for complementary pairs.
#    Time: O(n^3) average, Space: O(n)
#
# 3. Optimal: Fix two elements and use two pointers.
#    Time: O(n^3), Space: O(1) auxiliary*
#
# KEY LOGIC:
# Sort -> Fix two numbers -> Find the remaining pair.


class Solution:
    def fourSum(self, nums, target):

        nums.sort()  # Sort array to apply two-pointer technique

        result = []  # Store all unique quadruplets

        n = len(nums)  # Store total number of elements

        for i in range(n - 3):  # Fix the first element

            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicate first elements

            for j in range(i + 1, n - 2):  # Fix the second element

                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue  # Skip duplicate second elements

                left = j + 1  # Third element starts after second element

                right = n - 1  # Fourth element starts at the last position

                while left < right:  # Search while pointers do not cross

                    # Calculate the sum of all four selected elements
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total < target:
                        left += 1  # Increase sum by moving left forward

                    elif total > target:
                        right -= 1  # Decrease sum by moving right backward

                    else:
                        # Store the quadruplet when the sum matches target
                        result.append([
                            nums[i], nums[j], nums[left], nums[right]
                        ])

                        # Skip duplicate values at the left pointer
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1

                        # Skip duplicate values at the right pointer
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                        left += 1  # Move left to find another combination
                        right -= 1  # Move right to find another combination

        return result  # Return all unique quadruplets