# 1st Solution - Brute Force Approach
# The Brute Force Approach is a simple, straightforward method where we try all possible solutions without any optimization.
# - Time Complexity: O(k * n), where `n` is the length of the array and `k` is the number of rotations.
# - Space Complexity: O(1), as the algorithm modifies the input array in place without requiring extra space.
# - Performance: Slow for large values of `k`, as we perform `k` insertions and pop operations for each iteration.

from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # Iterate k times
        for i in range(1, k + 1):
            a = len(nums)  # Find the length of the array
            b = nums[a - 1]  # Get the last element of the array
            nums.insert(0, b)  # Insert the last element at the beginning of the array
            nums.pop()  # Remove the last element (which is now duplicated)

# Example Usage:
solution = Solution()  # Create an instance of the Solution class
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
solution.rotate(nums, k)  # Rotates the array nums by 3 steps
print(nums)  # Output: [5, 6, 7, 1, 2, 3, 4]


# 2nd Solution - Optimal Approach using List Slicing
# In this optimized approach, we use list slicing to perform the rotation in one step instead of multiple iterations.
# - Time Complexity: O(n), where `n` is the length of the array. Slicing takes O(n) time, and we are only doing it once.
# - Space Complexity: O(1), as the array is modified in place without using extra space.
# - Performance: Fast and efficient for large values of `k`, as it reduces the number of operations to a single slice and concatenation.

from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # Calculate the effective number of rotations (k % n)
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]  # Rotate the array by slicing and concatenating

# Example Usage:
solution = Solution()  # Create an instance of the Solution class
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
solution.rotate(nums, k)  # Rotates the array nums by 3 steps
print(nums)  # Output: [5, 6, 7, 1, 2, 3, 4]
