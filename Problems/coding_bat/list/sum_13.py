#Author: esau91
#Date: 19/02/2021
#Source: codingbat.com
#Description: Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.

def sum13(nums):
    my_sum = 0
    save_number = 0

    for i in range(len(nums)):
        if nums[i]== 13:
            save_number = 1
        elif not save_number:
            my_sum += nums[i]
        else:
            save_number = 0
      
    return my_sum

def main():
    sum13([13, 1, 2, 13, 2, 1, 13])
    sum13([13, 0, 13])
    SUM13([])

if __name__ == '__main__':
        main()
