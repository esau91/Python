def solution(test):
    
    letters = {}
    
    if len(test) < 1:
        print(0)
        return 0
    if len(test) == 1:
        print(test, 1)
        return test, 1

    for letter in test:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1

    print(letters)
    return letters

def main():
    solution('preguntame')
    solution('unodostrescuatro')
    solution('palabras')
    solution('')
    solution('holamundo')

if __name__ == '__main__':
    main()
