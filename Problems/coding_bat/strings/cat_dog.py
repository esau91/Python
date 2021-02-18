#Author: esau91
#Date: 17/02/2021
#Source: codingbat.com
#Description: Return True if the string "cat" and "dog" appear the same number of times in the given string.

def cat_dog(str):
    cat_counter = 0
    dog_counter = 0
    cat = 'cat'
    dog = 'dog'
    str_len = len(str)

    if str_len >= 3:
        for i in range(str_len - 2):
            if cat in str[i:i+3]:
                cat_counter += 1
            elif dog in str[i:i+3]:
                dog_counter += 1
              
    return cat_counter == dog_counter

def main():
    cat_dog('catxdogxdogxca')

if __name__ == '__main__':
    main()
