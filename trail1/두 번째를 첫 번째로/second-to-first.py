text = list(input())
t = text[1]
for i in range(1, len(text)):
    if text[i] == t:
        text[i] = text[0]
text = ''.join(text)
print(text)