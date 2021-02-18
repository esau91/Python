#Author: esau91
#Date: 17/02/2021
#Source: codingbat.com
#Description: Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.

def count_evens(nums):
    even_counter = 0
    for num in nums:
        if num % 2 == 0:
            even_counter += 1

    return even_counter

def main():
    count_evens([2, 11, 9, 0])

if __name__ == '__main__':
    main()
