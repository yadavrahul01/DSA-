# Problem: Find two lines that can hold the maximum amount of water.
#
# Example:
# height = [1,8,6,2,5,4,8,3,7]
# Output = 49
#
# APPROACHES:
# 1. Brute Force: Calculate area for every possible pair.
#    Time: O(n^2), Space: O(1)
#
# 2. Optimal: Use two pointers and move the shorter line.
#    Time: O(n), Space: O(1)
#
# FORMULA:
# Area = Width * Minimum Height
# Area = (right - left) * min(height[left], height[right])


class Solution:
    def maxArea(self, height):

        left = 0  # Start pointer at the first element

        right = len(height) - 1  # Start pointer at the last element

        max_area = 0  # Store the maximum water capacity found so far

        while left < right:  # Continue while both pointers are apart

            width = right - left  # Calculate distance between the two lines

            h = min(height[left], height[right])  # Shorter line limits water height

            area = width * h  # Calculate water area for current pair

            max_area = max(max_area, area)  # Update maximum area if current is larger

            if height[left] < height[right]:
                left += 1  # Move shorter left line to search for a taller one

            else:
                right -= 1  # Move shorter or equal right line inward

        return max_area  # Return the maximum water capacity