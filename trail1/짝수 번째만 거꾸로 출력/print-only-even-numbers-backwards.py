text = list(input())
arr = text[1::2]
arr.reverse()
for elem in arr:
    print(elem, end='')