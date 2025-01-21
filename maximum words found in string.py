# Approach: String Manipulation (Counting words by spaces)
# - This approach counts the number of spaces in each sentence, then adds 1 to determine the number of words in the sentence.
# - The sentence with the maximum number of words is returned as the result.

class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        # Use a generator expression to count spaces in each sentence, adding 1 to account for the last word
        return max(sentence.count(' ') + 1 for sentence in sentences)

# Example usage
sol = Solution()
print(sol.mostWordsFound(["alice and bob love coding", "i love leetcode", "stay hungry stay foolish"]))  # Output: 4

# Time Complexity: O(n * m), where n is the number of sentences, and m is the average length of a sentence.
# - Counting spaces takes O(m) time for each sentence, and we do this for each of the n sentences.
# Space Complexity: O(1), as we are only storing the maximum number of words at any given time.
