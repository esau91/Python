#Author: esau91
#Date: 03/04/2021
#Source: codingbat.com
#Description: return common characters from elements in list 

def commonChars(A):

    my_dict = {}
    intersect_dict = {}
    my_list = []

    if len(A) == A.count(A[0]):
        print(list(A[0]))
        return list(A[0])

    for element in A:
        if element not in my_dict:
            for letter in element:
                if my_dict.get(element, {}).get(letter, -1) >= 1:
                    my_dict[element][letter] += 1
                elif my_dict.get(element, {}) == {}:
                    my_dict[element] = {letter: 1}
                else:
                    my_dict[element][letter] = 1

    for k, v in my_dict.items():
        for letter, rep in v.items():
            if letter not in intersect_dict:
                intersect_dict[letter] = [rep]
            else:
                intersect_dict[letter].append(rep)

    for k, v in intersect_dict.items():
        if len(v) == len(A):
            my_list.extend(k * min(v))

    print(my_dict, intersect_dict, my_list)
    return my_list

def main():
     commonChars(["aaaaaaa","aaaaaaa","aaaaaaa"])
     commonChars(["3589a","ashkja","plmknj"])

if __name__ == '__main__':
    main()
