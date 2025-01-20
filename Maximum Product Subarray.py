# Approach: Brute Force (Generating all subarrays and computing products)
# - This approach generates all possible subarrays and calculates their product.
# - The maximum product from all subarrays is returned as the result.

from typing import List
import math

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        # Function to generate all possible subarrays
        def generate_subarrays(arr):
            subarrays = []
            # Iterate over all starting points of subarrays
            for i in range(len(arr)):
                # Iterate over all end points for each starting point
                for j in range(i, len(arr)):
                    subarrays.append(arr[i:j+1])  # Add the subarray to the list
            return subarrays  # Return all subarrays
        
        # Function to calculate the product of each subarray and find the maximum
        def multiply(sub_arrays):
            sub_arrays = generate_subarrays(nums)  # Generate all subarrays
            product = []
            # Iterate over all subarrays to calculate the product
            for i in sub_arrays:
                a = math.prod(i)  # Calculate the product of elements in the subarray
                product.append(a)  # Append the product to the list
            return max(product)  # Return the maximum product

        return multiply(nums)  # Call multiply function and return the result

# Example usage
sol = Solution()
print(sol.maxProduct([2, 3, -2, 4]))  # Output: 6 (subarray [2, 3] gives the maximum product)

# Time Complexity: O(n^3), where n is the length of `nums`.
# - Generating all subarrays takes O(n^2), and calculating the product for each subarray takes O(n) time.
# Space Complexity: O(n^2), as we are storing all subarrays in memory.
