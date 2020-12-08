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
                
                
                
#other
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Return if string is empty
        if not s: return s

        res = ""
        for i in range(len(s)):
            j = i + 1
            # While j is less than length of string
            # AND res is *not* longer than substring s[i:]
            while j <= len(s) and len(res) <= len(s[i:]):
                # If substring s[i:j] is a palindrome
                # AND substring is longer than res
                if s[i:j] == s[i:j][::-1] and len(s[i:j]) > len(res):
                    res = s[i:j]
                j += 1

        return res
