""" Problem Description:
Merge Strings Alternatively
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string 
is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string. """

""" Approach:
1. Identify the word with the longest length to set loop range
2. Create a single for-loop
3. Write an if condition: Set even numbers in range to word1 letters, set odd numbers in range to word2 letters.
 

"""

def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """


        #Determining the word with the longest length for proper loop range
        longest = max(len(word1), len(word2)) #useful to find max value between variables

        # Creating an empty string to hold merged words
        merged = ""

        # Use for-loop to access the retrieve word letters to merge
        for i in range(longest):
            if i < len(word1): #checks if its out of bounds and skips to the next condition if so
                merged += word1[i]

            if i < len(word2):
                merged += word2[i]
        
        return merged

        # This code ensures the loop doesn't go out of bounds, the index is within the corresponding word length, the letters are 
        # printed alternatively between words and merges the remaining letters in the event of unequal word lengths
        

    