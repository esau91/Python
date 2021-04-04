
def product_array(given_array):

    array_len = len(given_array)
    product = 1
    new_array = [0] * array_len
    count_zeros = 0

    for i in range(array_len):
        if given_array[i] == 0:
            count_zeros += 1
        else:
            product *= given_array[i]

    for i in range(array_len):
        if count_zeros == 1 and given_array[i] == 0:
            new_array[i] = product
        elif count_zeros == 0:
            new_array[i] = int(product / given_array[i])

    return new_array
    
if __name__ == '__main__':
    print(product_array([1, 2, 3, 4, 5]))
    print(product_array([3, 2, 1]))
    print(product_array([3, 0, 1]))
    print(product_array([1, 2, 0, 0]))
