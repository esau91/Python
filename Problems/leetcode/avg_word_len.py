#Author: esau91
#Date: 03/04/2021
#Source: leetcode
#Description: return the average word len from string

def solution(test):
    
    words_len = []
    test = test.split()
    if len(test) == 0:
        print(0)
        return 0
    for word in test:
        words_len.append(len(word))

    print(sum(words_len)/len(words_len))

def main():
    solution('hola como estas preguntame algo')
    solution('uno dos tres cuatro')
    solution('palabras largas programando corriendo')
    solution('')
    solution('holamundo')

if __name__ == '__main__':
    main()
