class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()  # Remove leading and trailing whitespace

        if not s:
            return 0  # Empty string

        sign = 1  # Positive sign by default
        i = 0

        # Check for optional sign character
        if s[i] == '-' or s[i] == '+':
            if s[i] == '-':
                sign = -1
            i += 1

        # Process digits until a non-digit character is encountered
        result = 0
        while i < len(s) and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1

        # Apply sign and handle out-of-range values
        result = sign * result
        result = max(min(result, 2**31 - 1), -2**31)

        return result