class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []  # stores list of [character, count] pairs

        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1

                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([char, 1])
        
        res = "".join(char * count for char, count in stack)
        return res
        