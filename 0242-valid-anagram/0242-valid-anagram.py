class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_count = {}

        # Count the occurrences of each character in s
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        # Decrement the count for each character in t
        for char in t:
            if char in char_count:
                char_count[char] -= 1
                if char_count[char] == 0:
                    del char_count[char]
            else:
                return False

        return len(char_count) == 0