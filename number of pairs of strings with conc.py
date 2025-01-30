# Approach: Brute-Force Pair Search
# - The idea is to check all possible pairs of strings (i, j) in the list nums, where i != j.
# - For each pair, the concatenated result (nums[i] + nums[j]) is compared with the target string.
# - If they match the target, the pair is added to the result list.

from typing import List
class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        abc = []  # List to store valid pairs that satisfy the condition
        for i in range(len(nums)):  # Loop through each element of the nums list for the first part of the pair
            for j in range(len(nums)):  # Loop through each element of the nums list for the second part of the pair
                a = nums[i]  # First string of the pair
                if nums[i] + nums[j] == target and i != j:  # Check if concatenated pair matches target and indices are different
                    abc.append([nums[i], nums[j]])  # Add the valid pair to the result list
        return len(abc)  # Return the count of valid pairs

# Time Complexity: O(n^2), where n is the length of the nums list. We are checking all pairs of elements.
# Space Complexity: O(n^2), since we store all valid pairs in the abc list (in the worst case).
