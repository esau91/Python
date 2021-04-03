def solution(sentence1, sentence2):
    words = {}
    sentence1 = sentence1.split()
    sentence2 = sentence2.split()

    for word in sentence1:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1

    for word in sentence2:
        if word in words:
            words[word] = 0
        else:
            words[word] = 1

    for idx, val in words.items():
        if val > 0:
            print(idx * val)

def main():
    solution('hola mundo como estas','hola esau como te va')
    solution('hi how are you','hi what are you doing')
    solution('hi hi como estas','muy bien')

if __name__ == '__main__':
    main()

