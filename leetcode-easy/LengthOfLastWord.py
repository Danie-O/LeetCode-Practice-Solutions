"""PROMPT:
    Given a string s consisting of words and spaces, return the length of the last word in the string.

    A word is a maximal substring consisting of non-space characters only.
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # split string and select unique words not equal to empty strings
        # st = [i for i in s.split(" ") if i != ""] 
        # return len(st[-1])

        # Another approach without looping through all words
        c = 0
        for i in s[::-1]: 
            #  start going through charcters from end of string
            # if we encounter a space, thats the start of the last word so return count of chars in that word(c)
            if i == " ":  
                if c >= 1:
                    return c
            else:
                c += 1
        return c
        

# Examples
s = Solution()

# Example 1:
str1 = "Hello World"
print(s.lengthOfLastWord(str1))
# Output: 5

# Example 2:
str2 = "   fly me   to   the moon  "
print(s.lengthOfLastWord(str2))
# Output: 4
# Explanation: The last word is "moon" with length 4.