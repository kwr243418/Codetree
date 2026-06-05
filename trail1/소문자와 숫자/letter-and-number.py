text = input()
for i in text:
    if i.isalpha():
        print(i.lower(), end='')
    elif i.isdigit():
        print(i, end='')