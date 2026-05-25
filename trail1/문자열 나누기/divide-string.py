n = int(input())
text = input()
lst = ""
for elem in text:
    if elem != ' ':
        lst += elem
for i in range(len(lst)):
    if i != 0 and i % 5 == 0:
        print()
    print(lst[i], end='')