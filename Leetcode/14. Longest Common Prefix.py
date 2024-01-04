class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        l = len(min(strs,key=len))
        strs.sort()
        for i in range(l):
            if(strs[0][i] == strs[-1][i]):
                res+=strs[0][i]
            else:
                break
        return res

        
