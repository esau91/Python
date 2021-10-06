'''
Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant extra space.
'''

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        dups = []
        nums_dict = {}
        
        for n in nums:
            if n in nums_dict:
                nums_dict[n] += 1
                dups.append(n)
            else:
                nums_dict[n] = 1
            
        return dups