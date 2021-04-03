
def reversed_string(string_1, string_2):
    
    #return True if string_1[::-1] == string_2 else False

    for i in range(len(string_1)):
        
        if string_1[i] != string_2[-i - 1]: 
            return False
    
    return True

if __name__ == '__main__':
    print(reversed_string('ABC', 'CBA'))
    print(reversed_string('ABCdf', 'fdCBA'))
    print(reversed_string('eABC', 'CBAi'))
