#1 sol
# using sorting
from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k-1]
# 2nd solution
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(1, k):
            nums.remove(max(nums))
        return max(nums)