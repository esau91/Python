
def find_missing(arr1, arr2):
    '''
    if len(arr2) >= 1:
        set_1 = set(arr1)
        set_2 = set(arr2)

        print(set_1.difference(set_2))
    else:
        print(None)
    '''
    ''' 
    len_arr1 = len(arr1)
    len_arr2 = len(arr2)

    if len_arr1 == len_arr2 - 1:
        bigger = arr2
        smaller = arr1
    elif len_arr2 == len_arr1 - 1:
        bigger = arr1
        smaller = arr2
    else:
        print(None)
        return 0
    
    sum_bigger = sum(bigger)
    sum_smaller = sum(smaller)

    missing_number = sum_bigger - sum_smaller

    if missing_number in bigger:
        print(missing_number)
    '''
    my_dict = {}

    for element in arr2:
        if element in my_dict:
            my_dict[element] += 1
        else:
            my_dict[element] = 1

    for element in arr1:
        if my_dict.get(element,0) == 0:
            print(element)
        else:
            my_dict[element] -= 1

def main():
    find_missing([1,2,3,4,5,6], [3,4,2,1,6])
    find_missing([1,2,4,4,2], [1,2,4,4])
    find_missing([1,2,3,4,5,6], [5,3,4,2,1,6])
    #find_missing([1,3,4], [3,4,2,1,6])

if __name__ == '__main__':
    main()
