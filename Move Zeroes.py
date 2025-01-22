# Approach: In-Place Rearrangement
# - The idea is to move all non-zero elements to the front and then fill the remaining elements with zeroes.
# - It iterates over the list once to move non-zero elements and keeps track of the position where the next non-zero element should go.

from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        abc = 0  # This will track the index where non-zero elements should be placed
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[abc] = nums[i]  # Place the non-zero element at the current 'abc' index
                abc += 1  # Move the 'abc' pointer forward
        # After all non-zero elements are placed, fill the remaining part of the list with zeroes
        for i in range(abc, len(nums)):
            nums[i] = 0

# Time Complexity: O(n), where n is the length of the list. We are iterating through the list twice.
# Space Complexity: O(1), since we are modifying the list in-place without using any extra space.
# Approach: List Comprehension (Practical)
# - This approach separates the non-zero elements and zeroes using list comprehension.
# - First, it creates a new list with only the non-zero elements, then appends the appropriate number of zeroes at the end.
# - Although not strictly in-place, this is a simple and effective solution.

from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Create a list of all non-zero elements from nums
        nums2 = [x for x in nums if x != 0]
        # Calculate how many zeroes need to be appended
        a = len(nums) - len(nums2)
        # Update nums to contain the non-zero elements followed by the appropriate number of zeroes
        nums[:] = nums2 + [0] * a

# Time Complexity: O(n), where n is the length of the list. We create a new list with non-zero elements and append zeroes.
# Space Complexity: O(n), as we are using an extra list to store the non-zero elements and the resulting list.
