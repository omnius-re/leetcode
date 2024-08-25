"""Difficulty level: Easy"""

"""Problem Description: Reverse Vowels of a String
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
"""

"""Approach:
Use Two-pointers to track vowels on both ends of the string and swap positions
"""

def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s) #convert to list since strings are immutable
        i, j = 0, len(s)-1 #two pointers i and j at the start and end of the string list

        while(i<j): #loop stops when both pointers meet
            if s[i] not in 'aeiouAEIOU': #checks for vowels
                i+=1
                continue
            elif s[j] not in 'aeiouAEIOU': #checks for vowels
                j-=1
                continue
            s[i], s[j] = s[j], s[i] #elements swap positions when both pointers meet a vowel
            i+=1
            j-=1


        return "".join(s) #joins list together back into string to return