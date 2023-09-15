class Solution:
    # O(2 ^ (2n)) time | O(2 ^ 2n) space
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(left, right, s):
            if left == right == n:
                res.append(s)
                return 

            # if left brackets < n, add left bracket
            if left < n:
                backtrack(left + 1, right, s + "(")

            # if right brackets < left brackets, add right bracket
            if right < left:
                backtrack(left, right + 1, s + ")")
            
        backtrack(0, 0, "")
        return res

    # O(2 ^ (2n)) | O(2n) space
    # def generateParenthesis(self, n: int) -> List[str]:
    #     stack = []
    #     res = []

    #     def backtrack(openN, closedN):
    #         if openN == closedN == n:
    #             res.append("".join(stack))
    #             return

    #         if openN < n:
    #             stack.append("(")
    #             backtrack(openN + 1, closedN)
    #             stack.pop()
    #         if closedN < openN:
    #             stack.append(")")
    #             backtrack(openN, closedN + 1)
    #             stack.pop()

    #     backtrack(0, 0)
    #     return res
            

        