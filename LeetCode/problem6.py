"""Difficulty level: Medium"""

"""Problem Description: Reverse Words in a String
Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. 
The returned string should only have a single space separating the words. Do not include any extra spaces."""

"""Approach:
1. Use split() to split the string of words by ' ' and store each word in a list
2. Use reverse() to reverse the order of words in the list
3. return string of words joined by ' ' using join()"""

def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        s_list = s.split()
        s_list.reverse()

        return " ".join(s_list)