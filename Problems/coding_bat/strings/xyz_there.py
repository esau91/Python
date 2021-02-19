#Author: esau91
#Date: 19/02/2021
#Source: codingbat.com
#Description: Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.).

def xyz_there(str):

    my_substr = 'xyz'
    len_str = len(str)

    if len_str >= 3:
        for i in range(len(str) - 2):
            substr = str[i:i+3]
            if my_substr == substr:
                if i == 0:
                    return True
                elif str[i -1] != '.':
                    return True

    return False


def main():
    xyz_there('1.xyz.xyz2.xyz')
    xyz_there('abc.xyzxyz')
    xyz_there('')


if __name__ == '__main__':
    main()
