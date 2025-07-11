# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        lower = 1
        higher = n
        if (n == 1):
            return 1
        while(higher >= lower):
            if (higher == lower):
                return higher
            guessed = (higher + lower)//2 + 1
            res = guess(guessed)
            if (res == 0):
                return guessed
            elif (res == 1):
                lower = guessed + 1 
            else:
                higher = guessed - 1

        