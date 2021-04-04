
def is_anagram(string_1, string_2):
    string_1 = string_1.lower().replace(' ','')
    string_2 = string_2.lower().replace(' ','')
    
    my_dict = {}
    
    if len(string_1) != len(string_2):
        return False

    for element in string_1:
        if element not in my_dict:
            my_dict[element] = 1
        else:
            my_dict[element] += 1

    for element in string_2:
        if element in my_dict:
            my_dict[element] -= 1
    
    if sum(list(my_dict.values())) == 0:
        return True
    else:
        return False

def main():
    print(is_anagram('Dog', 'God'))
    print(is_anagram('amar', 'A rma'))

if __name__ == '__main__':
    main()
