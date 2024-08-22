"""Difficulty level: Easy"""

"""Problem Description: 
Kids With the Greatest Number of Candies
There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.
Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.
Note that multiple kids can have the greatest number of candies."""

"""Approach:
1. Identify the largest element in the candies array and store it in a variable called max.
2. Iterate through array, add extra candies with each element and compare it against max
3. Append True if condition is met, False otherwise 
"""

def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max = 0
        sol = []

        for i in range(len(candies)): #finds maximum value by iterating through array
            if candies[i] > max:
                max = candies[i]

        for i in range(len(candies)): #iterates through loop and adds extracandy to each element before comparing against max
            if candies[i] + extraCandies >= max:
                sol.append(True) #appends boolean value
            else:
                sol.append(False) #appends boolean value

        return sol