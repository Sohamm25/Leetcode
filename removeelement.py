# Approach: Remove all occurrences of a specific value (val) from the list (nums)
# - We iterate through the list, checking for the target value (val).
# - If the value is found, we remove it from the list and increment a counter (i) to keep track of how many times the element has been removed.
# - After all the removals, we return the length of the modified list.

from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0  # Initialize a counter to track how many times `val` is removed
        for a in range(1, len(nums) + 1):  # Iterate over the list
            if val in nums:  # Check if `val` is present in the list
                nums.remove(val)  # Remove `val` from the list
                i += 1  # Increment the counter for each removal
        b = len(nums)  # Get the length of the modified list
        return b  # Return the new length of the list after removals

# Time Complexity: O(n*m), where n is the length of the list and m is the number of occurrences of `val`. Each `remove` operation takes O(n), and this could be repeated `m` times.
# Space Complexity: O(1), since the solution works in place and does not use extra space.
