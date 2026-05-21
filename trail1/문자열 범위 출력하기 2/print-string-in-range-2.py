text = input()
n = int(input())
if len(text) < n:
    for i in range(len(text)-1,-1,-1):
        print(text[i], end='')
else :
    for i in range(len(text)-1,len(text)-1-n,-1):
        print(text[i], end='')