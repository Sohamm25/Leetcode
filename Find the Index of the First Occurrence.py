# Approach: Naive String Matching (Brute Force)
# - This approach checks if `needle` is present in `haystack` using Python's `in` operator.
# - If present, it returns the index of the first occurrence using `index()`.
# - If not found, it returns -1.

from typing import List

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Check if the `needle` exists in `haystack`
        if needle not in haystack:
            return -1  # Return -1 if `needle` is not found
        else:
            # Use the index() method to find the first occurrence of `needle`
            print(haystack.index(needle))

# Example usage
sol = Solution()
sol.strStr("abcde", "cd")  # Output: 2

# Time Complexity: O(n * m), where n is the length of `haystack` and m is the length of `needle`.
# - Checking if `needle` exists takes O(n * m) in the worst case.
# - Finding the index of `needle` using index() is efficient when `needle` is small.
# Space Complexity: O(1), as no additional space is used other than variables.
