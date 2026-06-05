text = input()
arr = list(input())
for i in arr:
    if i == 'L':
        text = text[1:] + text[0]
    elif i == 'R':
        text = text[-1] + text[0:-1]
print(text)