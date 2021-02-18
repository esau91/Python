#Author: Esaú Reyes
#Source: condingbat.com
#Return the number of times that the string 'hi' appears anywhere in the given string

def count_hi(str):
    str_len = len(str)
    substr = 'hi'
    counter = 0
    if str_len >= 2:
        for i in range(str_len - 1):
            if substr in str[i:i+2]:
            counter += 1
        
    return counter

def main():
    count_hi('abc hi ho')

if __name__ == '__main__':
    main()
