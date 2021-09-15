#Merge two sorted arrays and returned sorted

def sorted_arrays(array_1, array_2):
    sorted_array = array_1 + array_2
    sorted_array.sort()
    
    return sorted_array

if __name__ == '__main__':
    array_1 = [0, 3, 4, 31]
    array_2 = [4, 6, 30]
    print(sorted_arrays(array_1, array_2))