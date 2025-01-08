# Problem: Check if an array contains any duplicate elements.
# - Return True if any value appears at least twice in the array.
# - Otherwise, return False.

# Solution 1: Using a set to detect duplicates
# - Time Complexity: O(n), where n is the length of nums.
#   - Converting the list to a set takes O(n), and comparing lengths is O(1).
# - Space Complexity: O(n), as the set requires additional storage.

from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Convert the list to a set and compare lengths
        # If lengths differ, duplicates are present
        return len(nums) != len(set(nums))

# Example usage
solution = Solution()
print(solution.containsDuplicate([1, 2, 3, 1]))  # Output: True (duplicate: 1)
print(solution.containsDuplicate([1, 2, 3, 4]))  # Output: False (no duplicates)

# Solution 2: Using a list to keep track of seen elements
# - Time Complexity: O(n^2) in the worst case.
#   - For each element in nums, checking if it exists in nums2 takes O(n).
# - Space Complexity: O(n), as nums2 stores additional elements.

from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums2 = []  # List to track seen elements
        for i in nums:
            if i in nums2:  # Check if the current element is already seen
                return True  # Duplicate found
            nums2.append(i)  # Add the current element to the seen list
        return False  # No duplicates found
