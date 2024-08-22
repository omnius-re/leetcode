def gcdOfStrings(self, str1, str2):

    len1 = len(str1)
    len2 = len(str2)
    sol = ""

    def isDivisor(i):
        if len1 % i != 0 or len2 % i != 0: #checks if length of sliced string is divisible for both strings
            return False
        f1, f2  = len1 // i, len2 // i #stores integer division value for the length of both strings
        return str1[:i] * f1 == str1 and str1[:i] * f2 == str2 #returns boolean by checking if sliced string is gcd for both strings

    for i in range(1, len(min(len1, len2)+1)):
        if isDivisor(i):
            sol = str1[:i]
    
    return sol
