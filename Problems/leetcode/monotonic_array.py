def solution(test):
   
    dec = 0
    inc = 0

    for i in range(len(test) - 1):
        if test[i] == test[i + 1]:
            continue
        elif test[i] < test[i+1] and not dec:
            inc = 1
        elif test[i] > test[i+1] and not inc:
            dec = 1
        else:
            print(False)
            return False
    print(True)
    return True

def main():
    solution([1,4,7,9,100])
    solution([50,20,6,-5])
    solution([1,1,1,1,1])
    solution([1,2,3,6,0])
    solution([90,45,2,-1,0])

if __name__ == '__main__':
    main()
