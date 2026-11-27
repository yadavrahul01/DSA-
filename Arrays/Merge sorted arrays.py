# Problem: Merge nums2 into nums1 in sorted order.
# nums1 has enough extra space at the end to hold nums2.
#
# Example:
# nums1 = [1, 2, 3, 0, 0, 0], m = 3
# nums2 = [2, 5, 6], n = 3
#
# Output:
# nums1 = [1, 2, 2, 3, 5, 6]
#
# APPROACHES:
# 1. Brute Force: Append nums2 and sort the entire array.
#    Time: O((m+n) log(m+n)), Space: Depends on sorting
#
# 2. Optimal: Compare elements from the end and fill nums1 backward.
#    Time: O(m+n), Space: O(1)
#
# PATTERN: Two Pointers + In-place Merging
#
# KEY LOGIC:
# Compare the largest remaining elements.
# Place the larger element at the last available position.
# Work backward to avoid overwriting unprocessed elements.


class Solution:
    def merge(self, nums1, m, nums2, n):

        i = m - 1  # Pointer to the last valid element in nums1

        j = n - 1  # Pointer to the last element in nums2

        k = m + n - 1  # Pointer to the last available position in nums1

        while i >= 0 and j >= 0:  # Continue while both arrays have elements

            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]  # Place larger nums1 element at the end
                i -= 1  # Move nums1 pointer backward

            else:
                nums1[k] = nums2[j]  # Place larger or equal nums2 element
                j -= 1  # Move nums2 pointer backward

            k -= 1  # Move the output position backward

        # Copy remaining nums2 elements if any are left
        while j >= 0:

            nums1[k] = nums2[j]  # Place remaining nums2 element

            j -= 1  # Move nums2 pointer backward

            k -= 1  # Move output position backward

        # Remaining nums1 elements are already in their correct positions