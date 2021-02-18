#Author: esau91
#Date: 17/02/2021
#Source: codingbat.com
#Description: Given a string, return a string where for every char in the original, there are two chars.

def double_char(str):
    new_str = ''
    for i in str:
        new_str += i * 2
                
    return new_str

def main():
    double_char('Hi-There')
    double_char('')

if __name__ == '__main__':
    main()
