class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""  # Empty input list

        # Find the minimum length among all strings
        min_length = min(len(s) for s in strs)

        # Compare characters at each index
        for i in range(min_length):
            char = strs[0][i]  # Get character from the first string
            if any(s[i] != char for s in strs[1:]):
                return strs[0][:i]  # Return the prefix until the current index

        return strs[0][:min_length]  # Return the entire shortest string as the prefix