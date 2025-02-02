# Approach: 
# - First, split the input string `s` into a list of words using the `split()` method, which by default splits by whitespace.
# - Then, reverse the list of words using the `reversed()` function.
# - Finally, join the reversed list of words back into a string, separating them with a single space using the `join()` method.

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()  # Split the input string into a list of words by whitespace
        abc = ' '.join(reversed(words))  # Reverse the list and join the words with a space between them
        return abc  # Return the resulting string with the words reversed

# Time Complexity: O(n), where n is the length of the input string. Splitting and joining operations take linear time.
# Space Complexity: O(n), as we need additional space to store the list of words and the final result.

# Example Outputs:
solution = Solution()
print(solution.reverseWords("the sky is blue"))  # Output: "blue is sky the"
print(solution.reverseWords("  hello world  "))  # Output: "world hello"
