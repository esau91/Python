#Author: esau91
#Date: 17/02/2021
#Source codingbat.com
#Description: Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. Use int division to produce the final average. You may assume that the array is length 3 or more.


def centered_average(nums):
    new_nums = []
    nums.sort()
          
    new_nums = nums[1:-1]
    avg = int(sum(new_nums) / len(new_nums))
                
    return avg

def main():
    centered_average([100, 0, 5, 3, 4])
    centered_average([4, 4, 4, 4, 5])

if __name__ == '__main__':
    main()

