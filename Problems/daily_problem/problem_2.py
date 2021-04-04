
def product_array(given_array):

    back = 1
    array_len = len(given_array)
    new_array = [] 

    for i in range(array_len):
        if i > 0:
            back *= given_array[i - 1]
        front = 1
        for j in range(i + 1, array_len):
            front *= given_array[j]

        new_array.append(back * front)

    return new_array
    
if __name__ == '__main__':
    print(product_array([1, 2, 3, 4, 5]))
    print(product_array([3, 2, 1]))
