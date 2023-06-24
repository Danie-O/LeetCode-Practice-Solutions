class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
            TIME COMPLEXITY: 
                O(log(n)) => the value of n decreases by half, for each iteration in the while loop
            SPACE COMPLEXITY: 
                O(1) => asides the result, isNegative and abs(n) variables, no extra space(DS) is used 
        """ 
        neg = True if n < 0 else False
        result = 1
        n = abs(n)

        while n:
            if n % 2 == 1:
                result *= x
            x *= x
            n //= 2
        return result if not neg else 1 / result

