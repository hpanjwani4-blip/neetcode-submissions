class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re

        s = re.sub(r'[^a-zA-Z0-9]', '', s).upper()
        r = 0 
        l = len(s)-1
        while r<=l:
            if s[r]!=s[l]:
                return False
            
            r+=1;
            l-=1;

        return True
        