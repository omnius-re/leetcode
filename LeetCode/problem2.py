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
