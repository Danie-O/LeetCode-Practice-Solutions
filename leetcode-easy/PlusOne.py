from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #if the least digit in digits doesnt become a 'tenth'after adding 1
        if digits[-1] + 1 < 9:
            digits[-1] = digits[-1] + 1
            return digits
        else:
            total = 0

            # convert single number in array to an integer
            if len(digits) == 1:
                total = digits[0]
            # convert entire array to integer by iterating through and multiplying by appropriate power of 10
            else:
                index = 0
                for power in range(len(digits)-1, -1, -1):
                    total += digits[index] * (10 ** power)
                    index += 1
            #add 1 to resulting digit(total)
            total += 1
            # convert total to string
            total = str(total)

            # create a list of the integer values of each character in converted string (total)
            result = [int(total[i]) for i in range(len(total))]
            return result
            
# Case 1:
digits = [4,3,2,1]
