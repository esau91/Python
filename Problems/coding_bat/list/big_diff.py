#Author: esau91
#Date: 17/02/2021
#Source: codingbat.com
#Description: Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array.

def big_diff(nums):
      
    if len(nums) >= 2:
        nums.sort()
        smallest = nums[0]
        largest = nums[-1]

        if smallest != largest:
            return largest - smallest

    return 0

def main():
    big_dif([7, 7, 6, 8, 5, 5, 6])
    big_dif([2])

if __name__ == '__name__':
    main()
