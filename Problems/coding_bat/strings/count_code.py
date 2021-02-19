#Author: esau91
#Date: 17/02/2021
#Source: codingbat.com
#Description: Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.

def count_code(str):
      
    my_sbstr = 'coe'
    counter = 0

    for i in range(len(str) - 3):
        substr = list(str[i:i+4])
        substr.pop(2)
        substr = ''.join(substr)
        if my_sbstr == substr:
          counter += 1
    
    return counter

def main():
    count_code('AAcodeBBcoleCCccorfDD')
    count_code('cozcop')
    count_code('')

if __name__ == '__main__':
    main()

