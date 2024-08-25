"""Difficulty level: Medium"""

"""Problem Description: Product of Array Except Self
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation."""

"""Approach:
1. Create three arrays with 1s to store prefix, suffix and result product values
2. For-loop to calculate prefix products of index i using a method that uses previously performed calculations to find product
3. For-loop to calculate suffix products the same way
4. Multiply prefix and suffix iteratively and store it in result before returning it"""

def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        prefix = [1] * n #prefix array that will store product of all values before index i
        suffix = [1] * n #suffix array that will store product of all values after index i
        result = [1] * n #multiply prefix and suffix to find product result

        for i in range(1, n): #starts from 1 since there is no prefix product before index 0
            prefix[i] = prefix[i-1] * nums[i-1] #multiplies previously calculated prefix product value and the value right before nums[i]  
        
        for i in range(n-2, -1, -1): #starts from n-2 since index n is out of bounds and index n-1 has no suffix value
            suffix[i] = suffix[i+1] * nums[i+1] #multiplies previously calcualted suffix product value and the value right after nums[i]
        
        for i in range(n): #iteratively calculates result of prefix * suffix
            result[i] = prefix[i] * suffix[i]
            
        
        return result

"""Learnings:
Initially used nums[:i][i+1:] and np.prod() function to calculate all product values except nums[i].
However the runtime is not efficient and there are redundant calculations when calculating product for each index.
Prefix and Suffix product calculation allows to use previously done calculations to find result values in linear time"""