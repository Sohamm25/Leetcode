# Problem: Find and Replace Pattern
# - Given a list of words and a pattern, return the words that match the pattern.
# - Two words match the pattern if they can be transformed into the same pattern.
#   - Example: "abc" matches "mno" but not "mee".

class Solution:
    def findAndReplacePattern(self, words: list[str], pattern: str) -> list[str]:
        # Helper function to generate the numeric pattern of a word
        # - Assigns each unique character in the word a unique number.
        # - Example: "abc" -> [0, 1, 2], "mee" -> [0, 1, 1]
        def get_pattern(word):
            mapping = {}  # Maps characters to unique integers
            return [mapping.setdefault(char, len(mapping)) for char in word]

        # Get the numeric pattern of the input pattern
        rep = get_pattern(pattern)

        # Filter and return words that match the numeric pattern
        return [word for word in words if get_pattern(word) == rep]

# Example usage
solution = Solution()
print(solution.findAndReplacePattern(["abc", "deq", "mee", "aqq", "dkd", "ccc"], "abb"))  # Output: ["mee", "aqq"]

# Time Complexity: O(n * m), where n is the number of words and m is the average length of a word.
# - Generating the numeric pattern for each word takes O(m).
# - Comparing patterns for all words takes O(n * m).
# Space Complexity: O(n * m), as each word's pattern is stored temporarily.
