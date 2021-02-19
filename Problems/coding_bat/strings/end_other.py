#Author: esau91
#Date: 17/02/2021
#Source: codingbat.com
#Description: Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive").

def end_other(a, b):
      
    a = a.lower()
    b = b.lower()
    len_a = len(a)
    len_b = len(b)


    if a == b:
        return True
    elif len_a > len_b and a[-len_b:] == b:
        return True
    elif len_b > len_a and b[-len_a:] == a:
        return True
    else:
        return False

def main():  
    end_other('xyz', '12xyz')
    end_other('12', '12')
    end_other('Hiabcx', 'bc')


if __name__ == '__main__':
    main()
