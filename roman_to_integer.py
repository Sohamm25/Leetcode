# Approach:
# - We maintain a dictionary `roman_values` that maps each Roman numeral (and valid two-character numerals like "IV", "IX", etc.) to its integer value.
# - We iterate through the input string `s`. If we encounter a two-character numeral (like "IV" or "IX"), we add its corresponding value to the result.
# - If the two-character numeral is not found, we add the value of the current single character numeral to the result.
# - Finally, we return the sum of the values, which gives the integer representation of the Roman numeral.

class Solution:
    def romanToInt(self, s: str) -> int:
        # Roman numeral to integer mappings, including both single characters and two-character numerals
        roman_values = {
            "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900,
            "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
        }
        
        abc = []  # List to store the integer values of the Roman numerals

        i = 0  # Initialize the index to start iterating over the string `s`
        while i < len(s):  # Iterate through the string `s` until the end
            # Check if the current and next character form a valid two-character Roman numeral
            if i + 1 < len(s) and s[i:i+2] in roman_values:
                abc.append(roman_values[s[i:i+2]])  # Append the value for the two-character numeral
                i += 2  # Skip the next character since we've already processed it
            else:
                abc.append(roman_values[s[i]])  # Append the value for the single character numeral
                i += 1  # Move to the next character

        return sum(abc)  # Return the sum of the values as the integer representation

# Time Complexity: O(n), where n is the length of the input string `s`. We iterate through the string once.
# Space Complexity: O(n), where n is 
