
def second_largest(given_list):

    my_set = set(given_list)
    give_list = list(my_set) 

    if len(given_list) < 2:
        return None
    else:       
        given_list.sort()
        return given_list[-2]

if __name__ == '__main__':
    print(second_largest([1, 3, 4, 5, 0, 2]))
    print(second_largest([3, 4, 4, 7, 1, 1, 0]))
