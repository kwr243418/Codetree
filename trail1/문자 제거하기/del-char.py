text = list(input())
while len(text) > 1:
    n = int(input())
    if n >= len(text):
        text.pop()
        print(''.join(text))
    else :
        text.pop(n)
        print(''.join(text))