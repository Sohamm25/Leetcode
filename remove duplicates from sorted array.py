# Approach: Remove Duplicates using a new list (nums2)
# - We iterate through the original list and keep adding elements to a new list (nums2) only if they are not already present.
# - Then, we copy the elements back from the new list (nums2) to the original list (nums).
# - Finally, we return the length of the new list, which will contain only the unique elements.

from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums2 = []  # Initialize an empty list to store unique elements
        for i in nums:
            if i not in nums2:  # Check if the element is already in nums2
                nums2.append(i)  # Add it to nums2 if not already present
        # Copy the unique elements back into the original list (nums)
        for i in range(len(nums2)):
            nums[i] = nums2[i]
        return len(nums2)  # Return the length of the list with unique elements

# Time Complexity: O(n^2), where n is the length of the input list `nums` because checking `if i not in nums2` takes O(n) for each element.
# Space Complexity: O(n), because we use an additional list `nums2` to store the unique elements.
