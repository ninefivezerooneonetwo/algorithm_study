word = input()
alphabet = list(range(97, 123))

for i in alphabet:
    print(word.count(chr(i)))