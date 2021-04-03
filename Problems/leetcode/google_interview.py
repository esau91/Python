

def find_shortest(given_dict):
    
    shortest = {}
    iteration = 0
    flag = True

    while flag: 

        for key, value in given_dict.items():
            key_len = len(key)
            if iteration < key_len:
                key_subs = key[:iteration]
            print(key_subs)

            if key_subs not in shortest:
                shortest[key_subs] = shortest.get(key_subs, 1)
            else:
                shortest[key_subs] = shortest.get(key_subs, 1) + 1
            
            iteration += 1

    return shortest


if __name__ == '__main__':
    output = find_shortest({'boat' : 1, 'car' : -1, 'candy' : 10, 'home' :  9})
    print(output)
