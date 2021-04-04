def unique_pairs(my_arr, tgt):
    
    seen = set()
    output = set()

    if len(my_arr) < 2:
        return False

    for num in my_arr:
        target = tgt - num
        
        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num,target), max(num,target)))


    print('\n'.join(map(str, list(output)))) 


def main():
    unique_pairs([1,3,5,7,2,8], 9)
    unique_pairs([1,3,2,2], 4)

if __name__ == '__main__':
    main()
