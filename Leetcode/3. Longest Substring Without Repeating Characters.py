class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = ""
        max_length = 0

        for char in s:
            if char not in res:
                res += char
                max_length = max(max_length, len(res))
                print(max_length)
            else:
                # Start a new substring after the repeated character
                res = res[res.index(char) + 1:] + char
                print(res)
        print(max_length)
        return max_length
