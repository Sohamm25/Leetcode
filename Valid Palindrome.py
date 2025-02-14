# 1st Solution - Brute Force Approach for Palindrome Check
# This approach iterates over a predefined list of unwanted characters and removes them from the string.
# Then, it checks if the string is equal to its reverse to determine if it's a palindrome.
# - Time Complexity: O(n), where `n` is the length of the input string, because we process each character.
# - Space Complexity: O(n), due to the modified string.
# - Performance: Fairly good for small to medium-sized inputs.

from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # List of unwanted characters that need to be removed from the string
        unwanted_chars = [',', '!', ':', ';', '.', '?', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '{', '}', '[', ']', '|', '\\', '<', '>', '/', '`', '~', '"', "'"]
        
        # Remove unwanted characters
        for char in unwanted_chars:
            s = s.replace(char, "")
        
        # Remove spaces and convert to lowercase
        s = s.replace(" ", "").lower()
        
        # Check if the string is a palindrome by comparing it with its reverse
        return s == s[::-1]

# Example Usage:
so = Solution()  # Create an instance of the Solution class
result = so.isPalindrome("race a car")  # Check if the input string is a palindrome
print(result)  # Output: False
