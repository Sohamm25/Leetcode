# Approach: String Manipulation (Strip and Split)
# - This approach removes any leading or trailing whitespace from the string.
# - It then splits the string into a list of words and returns the length of the last word.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Remove leading and trailing whitespace from the string
        s = s.strip()
        
        # Split the string into words using whitespace as the delimiter
        words = s.split()
        
        # Return the length of the last word
        return len(words[-1])

# Example usage
sol = Solution()
print(sol.lengthOfLastWord("Hello World "))  # Output: 5

# Time Complexity: O(n), where n is the length of the string `s`.
# - Stripping and splitting the string both take linear time.
# Space Complexity: O(n), as the split operation creates a list of words.
