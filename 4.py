# my sol
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s :return s 
        sub=[] 
        ver=[]
        res=0
        for x in range(len(s)):
            sublength=x+1
            for i in range(len(s)-x):
                sub.append(s[i:i+sublength])
        for ss in sub:
            liss=list(ss)
            lissr=list(liss)
            lissr.reverse()
            if(liss==lissr):
                ver.append(ss)
        
        #make compare
        ver.reverse()
        lennn=len(ver[0])
        for ss in ver:
            lenn=len(ss)
            if lenn!=lennn:
                res=ver.index(ss)-1
                break
        return ver[res]
                
                
                
