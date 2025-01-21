# Approach: Merging and Sorting
# - This approach combines the two lists, nums1 and nums2, into one list.
# - After merging, the list is sorted to maintain the ascending order.

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Modify nums1 in-place by combining the first m elements with nums2
        nums1[:] = nums1[:m] + nums2  
        # Sort the combined list to ensure the elements are in ascending order
        nums1.sort()

# Example usage
sol = Solution()
nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
sol.merge(nums1, 3, nums2, 3)
print(nums1)  # Output: [1, 2, 2, 3, 5, 6]

# Time Complexity: O((m + n) * log(m + n)), where m and n are the lengths of nums1 and nums2 respectively.
# - Merging the lists takes O(m + n) time, and sorting the merged list takes O((m + n) * log(m + n)) time.
# Space Complexity: O(m + n), as we are storing the combined list in nums1.
