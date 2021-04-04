
def lowest_positive(given_list):
    unique_values = list(set(given_list))
    unique_values.sort(reverse = True)
    value = None 

    for i in range(len(unique_values)):
        if unique_values[i] < 0:
            del unique_values[i]
    
    unique_values.sort()    
    print(unique_values)

    for j in range(0, unique_values[-1]):
        if j in unique_values:
            pass
        else:
            value = j
            break

    if value == None:
        value = unique_values[-1] + 1
    
    return value

if __name__ == '__main__':
    print(lowest_positive([3, 4, -1, 1]))
    print(lowest_positive([1, 2, 0]))
    print(lowest_positive([10, -34, 8, 9, 0]))
