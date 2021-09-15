#Reverse a string

def reverse_string(my_string):
    my_words = my_string.split(' ')
    reversed_words = []
    for word in my_words:
        reversed_words.insert(0, word[::-1])

    return ' '.join(reversed_words)

if __name__ == '__main__':
    my_string = 'Hello My Name is Esaú'
    print(reverse_string(my_string))
