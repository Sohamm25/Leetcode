# 1st solution - Brute Force ApproachThe Brute Force Approach is a straightforward problem-solving method that systematically explores,
# all possible solutions to find the correct one. 
# It involves trying every possible combination or configuration without applying any advanced optimizations or heuristics.
# - Checks every pair of numbers to find the target sum.
# - Time Complexity: O(n^2)
# - Space Complexity: O(1)
# - Performance: Slow, approx 1684 ms.

from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# 2nd solution - Hash Map Approach
# - Uses a dictionary to find the target sum quickly.
# - Time Complexity: O(n)
# - Space Complexity: O(n)
# - Performance: Fast, approx 54 ms.

from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num = {}
        for i, j in enumerate(nums):
            abc = target - j
            if abc in num:
                return [num[abc], i]
            num[j] = i
#In short, self is crucial for making instance-specific variables and methods work correctly in a class.
#Without self, you lose the ability to store and access instance-specific data,
#leading to errors or unintended behavior.
