import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Convert to lowercase
        s = s.lower()

        # Remove non-alphanumeric characters
        s = re.sub('[^a-z0-9]', '', s)

        # Check if the string is equal to its reverse
        return s == s[::-1]