class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        newlst = []
        max_length = 0
        for i in s:
            while i in newlst:
                newlst.pop(0)
            newlst.append(i)
            max_length = max(max_length, len(newlst))
        return max_length