# 1st Solution - Brute Force Approach
# This approach first removes duplicates by converting the list into a set, and then handles different cases based on the length of the list.
# - Time Complexity: O(n log n), where `n` is the length of the list, due to the sorting operation.
# - Space Complexity: O(n), due to the set being used to remove duplicates.
# - Performance: Fairly slow for large inputs due to the sorting step.

from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))  # Remove duplicates by converting the list to a set
        if len(nums) == 1:
            print(nums[0])  # If only one unique number, return that number
        elif len(nums) == 2:
            a = sorted(nums)  # If only two unique numbers, sort and return the second largest
            print(a[1])
        else:
            a = sorted(nums)  # If more than two unique numbers, sort and return the third largest
            print(a[-3])

# Example Usage:
b = Solution()  # Create an instance of the Solution class
b.thirdMax([2, 3, 4, 5, 6, 7])  # Input a list and find the third largest unique number
# Output: 5
