#[2,5,1,2,3,5,1,2,4] -> 2
#[2,1,1,2,3,5,1,2,4] -> 1
#[2,3,4,5] -> Undefined

def recurring_number(input_arr):
    my_numbers = {}

    if len(input_arr) <= 1:
        return 'Undefined'

    for number in input_arr:
        if number not in my_numbers:
            my_numbers[number] = 1
        else:
            return number
    
    return 'Undefined'

if __name__ == '__main__':
    output = recurring_number([2,3,4,5])
    print(output)