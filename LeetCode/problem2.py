"""Difficulty level: Easy"""

"""Problem Description:
Greatest Common Divisor of Strings
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).
Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2."""

"""Approach:
1. Iterate through the strings using the minimum string length to avoid out of range error
2. Try out different combinations of string splices iteratively and check if they are divisible
3. Create a divisible funciton that checks for gcd by modular operation and factors to multiply to get the right output"""

def gcdOfStrings(self, str1, str2):

    len1 = len(str1)
    len2 = len(str2)
    sol = ""

    def isDivisor(i): #uses for-loop's range value to test strings

        if len1 % i != 0 or len2 % i != 0: #checks if sliced string length is divisible for both strings
            return False
        f1, f2  = len1 // i, len2 // i #stores integer division value for the length of both strings
        return str1[:i] * f1 == str1 and str1[:i] * f2 == str2 #returns boolean by checking if sliced string is gcd for both strings

    for i in range(1, len(min(len1, len2)+1)): #starts from 1 to minimum between string lengths and increments by 1
        if isDivisor(i): #calls funciton to check if the condition is met
            sol = str1[:i]
    
    return sol
