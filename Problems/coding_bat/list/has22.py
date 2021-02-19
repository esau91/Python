#Author: esau91
#Date: 19/02/2021
#Source: codingbat.com
#Description: Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.

def has22(nums):

    two = 0

    for i in range(len(nums)):
        if nums[i] == 2 and two:
            return True
        elif nums[i] == 2:
            two = 1
        elif two and nums[i] != 2:
            two = 0

    return False

def main():
    has22([4, 2, 4, 2, 2, 5])
    has22([5, 2, 5, 2])
    has22([])

if __name__ == '__main__':
    main()
