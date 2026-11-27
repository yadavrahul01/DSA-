# Problem: Calculate x raised to the power n (x^n).
#
# Example:
# x = 2.00000, n = 10
# Output = 1024.00000
#
# APPROACHES:
# 1. Brute Force: Multiply x by itself n times.
#    Time: O(n), Space: O(1)
#
# 2. Optimal: Use Binary Exponentiation (Fast Power).
#    Time: O(log n), Space: O(1)
#
# PATTERN: Binary Exponentiation + Divide and Conquer
#
# KEY LOGIC:
# If n is even: x^n = (x*x)^(n/2)
# If n is odd: Multiply the result by x.
# For negative n: x^(-n) = 1 / x^n


class Solution:
    def myPow(self, x, n):

        if n < 0:
            x = 1 / x  # Convert negative exponent into reciprocal
            n = -n  # Make exponent positive

        result = 1  # Store the final calculated power

        while n > 0:  # Continue until exponent becomes zero

            if n % 2 == 1:
                result *= x  # Multiply result when exponent is odd

            x *= x  # Square the base to calculate powers faster

            n //= 2  # Divide exponent by two in every iteration

        return result  # Return the calculated value of x raised to n