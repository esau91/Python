

def find_sum(given_list, target):

    for j in range(len(given_list) - 1): 
        for i in range(j + 1, len(given_list)):
            my_sum = given_list[j] + given_list[i]
            if my_sum == target:
                print(given_list[j], given_list[i])
                return True

if __name__ == '__main__':
    
    find_sum([10, 15, 3, 7], 17)
    find_sum([1, 15, -3, 20], 17)
