# Problem: Search for a target in a sorted 2D matrix.
#
# Example:
# matrix = [[1, 3, 5, 7],
#           [10, 11, 16, 20],
#           [23, 30, 34, 60]]
# target = 16
# Output = True
#
# APPROACHES:
# 1. Brute Force: Check every matrix element.
#    Time: O(m*n), Space: O(1)
#
# 2. Row-wise Binary Search: Search each row separately.
#    Time: O(m*log(n)), Space: O(1)
#
# 3. Optimal: Treat matrix as a sorted 1D array.
#    Time: O(log(m*n)), Space: O(1)
#
# KEY LOGIC:
# row = mid // n
# col = mid % n


class Solution:
    def searchMatrix(self, matrix, target):

        m = len(matrix)  # Calculate total number of rows

        n = len(matrix[0])  # Calculate total number of columns

        left = 0  # First index of imaginary 1D array

        right = m * n - 1  # Last index of imaginary 1D array

        while left <= right:  # Continue while search space is valid

            mid = (left + right) // 2  # Find middle index

            row = mid // n  # Convert 1D index into matrix row

            col = mid % n  # Convert 1D index into matrix column

            value = matrix[row][col]  # Access the middle matrix element

            if value == target:
                return True  # Target found, so return True

            elif value < target:
                left = mid + 1  # Search the right half

            else:
                right = mid - 1  # Search the left half

        return False  # Target does not exist in the matrix