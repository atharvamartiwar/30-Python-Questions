class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_count = {}

        # Count the occurrences of each character
        for i in range(len(s)):
            char = s[i]
            char_count[char] = char_count.get(char, 0) + 1

        # Find the first character with count 1
        for i in range(len(s)):
            char = s[i]
            if char_count[char] == 1:
                return i

        return -1