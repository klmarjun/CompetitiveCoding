class Solution:
    def longestPalindrome(self, s: str) -> str:
        li=[]
        for i in range(len(s)):
            li.append(self.findPal(s,i,i))
            li.append(self.findPal(s,i,i+1))
        if li:
            return max(li,key=lambda x:len(x))
        return s[0]
    def findPal(self,s,j,k):
        while(j>=0 and k<len(s) and s[j]==s[k]):
            j-=1
            k+=1
        return s[j+1:k]
        