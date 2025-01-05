# Problem: Find the maximum area of water a container can store.
# - Each element in the list represents the height of a vertical line.
# - The area is determined by the shorter line and the distance between the lines.

from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Initialize two pointers and a variable to store the maximum area
        left = 0  # Pointer starting at the left end
        right = len(height) - 1  # Pointer starting at the right end
        max_area = 0  # Variable to track the maximum area found
        
        # Use a two-pointer approach to calculate the maximum area
        while left < right:
            # Calculate the current area based on the shorter line and the distance
            current_area = min(height[left], height[right]) * (right - left)
            # Update the maximum area if the current area is larger
            max_area = max(max_area, current_area)
            
            # Move the pointer pointing to the shorter line inward
            if height[left] < height[right]:
                left += 1  # Move the left pointer to the right
            else:
                right -= 1  # Move the right pointer to the left
        
        return max_area  # Return the maximum area found
