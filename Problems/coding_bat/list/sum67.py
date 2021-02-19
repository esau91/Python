#Author: esau91
#Date: 19/02/2021
#Source: codingbat.com
#Description: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.

def sum67(nums):

    flag = 0
    my_sum = 0

    for i in range(len(nums)):
        if nums[i] == 6:
            flag = 1
        elif not flag:
            my_sum += nums[i]
        elif nums[i] == 7:
            flag = 0
                    
    return my_sum

def main():
    sum67([6, 7, 1, 6, 7, 7])
    sum67([1, 6, 2, 2, 7, 1, 6, 99, 99, 7])
    sum67([])

if __name__ == '__main__':
        main()
