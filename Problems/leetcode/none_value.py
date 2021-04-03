def solution(test):
    prev = None 
    new_list = []
    if len(test) > 1:
        for idx, val in enumerate(test):
            if idx > 0 and val is None:
                new_list.append(prev)
            else:
                new_list.append(val)

            if val is not None:
                prev = val
        print(new_list)
    
    else:
        print(test)

def main():
    solution([None,1,3,4,5])
    solution([0,1,None,4,5])
    solution([None,1,3,4,None])
    solution([0,None,None,4,5])
    solution([None,None])
    solution([None])

if __name__ == '__main__':
    main()

