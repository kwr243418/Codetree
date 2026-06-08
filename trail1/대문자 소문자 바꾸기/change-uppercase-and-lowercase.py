text = input()
for i in text:
    if 'A' <= i and i <= 'Z':
        print(i.lower(), end='')
    else :
        print(i.upper(), end='')