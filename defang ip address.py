# Problem: Defang an IP Address
# - Replace every period (".") in a given IP address with "[.]".
# - This transformation is often used to prevent IP addresses from being interpreted or rendered as hyperlinks.

class Solution:
    def defangIPaddr(self, address: str) -> str:
        # Use the string replace() method to replace "." with "[.]"
        return address.replace(".", "[.]")

# Example usage
solution = Solution()
print(solution.defangIPaddr("1.1.1.1"))  # Output: "1[.]1[.]1[.]1"
print(solution.defangIPaddr("192.168.0.1"))  # Output: "192[.]168[.]0[.]1"

# Time Complexity: O(n), where n is the length of the input string.
# - The replace() function processes the entire string in one pass.
# Space Complexity: O(n), as the output string requires additional space.
