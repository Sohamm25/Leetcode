# Approach: Recursive Approach to Plus One
# - The idea is to start from the least significant digit (the last element of the list) and add one.
# - If a digit becomes 10 (i.e., 9 + 1), it is set to 0 and we recursively move to the next more significant digit (i.e., left).
# - If we reach the most significant digit and it becomes 10, we insert a 1 at the beginning of the list.

from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        def af(index):
            # Base case: If index is negative, it means we need to add a new most significant digit
            if index < 0:
                digits.insert(0, 1)  # Insert '1' at the beginning
                return
            # If the current digit is 9, set it to 0 and recursively move left
            if digits[index] == 9:
                digits[index] = 0
                af(index - 1)  # Recur for the next left digit
            else:
                # Otherwise, simply add 1 to the current digit
                digits[index] += 1
                return  # Return as no further recursion is needed
        
        # Start recursion from the least significant digit (last element)
        af(len(digits) - 1)
        return digits  # Return the modified list

# Time Complexity: O(n), where n is the length of the digits list. In the worst case, the recursion goes through all digits.
# Space Complexity: O(n), for the recursion stack and list modifications (insertion at the beginning in worst case).
