class Solution:
    def isPalindrome(self, s: str) -> bool:
        # word = ""

        # for c in s:
        #     if c.isalnum():
        #         word += c.lower()
            
        # return word == word[::-1]

        l,r = 0, len(s)-1

        while l < r:
            while l<r and not self.isAlphanumeric(s[l]):
                l += 1
            while r>l and not self.isAlphanumeric(s[r]):
                r -= 1
                
            if s[l].lower() != s[r].lower():
                return False
            l,r = l+1, r-1
        return True
            
    def isAlphanumeric(self, c):
            return (c.isalnum())    #ord("A") <= ord(c) <= ord("Z") or 
                                    #ord("a") <= ord(c) <= ord("z") or
                                    #ord("0") <= ord(c) <= ord("9")


