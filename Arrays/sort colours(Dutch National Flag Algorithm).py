# Problem: Sort an array containing only 0, 1 and 2.
#
# Example:
# nums = [2, 0, 2, 1, 1, 0]
# Output = [0, 0, 1, 1, 2, 2]
#
# APPROACHES:
# 1. Brute Force: Use a built-in sorting algorithm.
#    Time: O(n*log(n)), Space: Depends on sorting
#
# 2. Better: Count 0s, 1s and 2s, then overwrite the array.
#    Time: O(n), Space: O(1)
#
# 3. Optimal: Dutch National Flag Algorithm.
#    Time: O(n), Space: O(1)
#
# KEY LOGIC:
# low  -> Position for 0
# mid  -> Current element
# high -> Position for 2


class Solution:
    def sortColors(self, nums):

        low = 0  # Boundary for the next zero

        mid = 0  # Current element being checked

        high = len(nums) - 1  # Boundary for the next two

        while mid <= high:  # Continue until the unknown region is empty

            if nums[mid] == 0:

                # Move zero to the beginning of the array
                nums[low], nums[mid] = nums[mid], nums[low]

                low += 1  # Expand the region of zeros

                mid += 1  # Current element is now processed

            elif nums[mid] == 1:

                # One is already in the correct middle region
                mid += 1  # Move to the next element

            else:

                # Move two to the end of the array
                nums[mid], nums[high] = nums[high], nums[mid]

                high -= 1  # Shrink the region for unknown elements

                # Do not increment mid here because the swapped element
                # from the high position has not been checked yet