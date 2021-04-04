
def find_values(given_list, target):

    for i in range(len(given_list) - 1):

        result = target - given_list[i]
        
        if result in given_list:
            print(given_list[i], result)

if __name__ == '__main__':

    find_values([10, 15, 3, 7], 17)
