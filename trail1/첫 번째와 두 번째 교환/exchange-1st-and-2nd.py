text = input()
t1 = text[0]
t2 = text[1]
text = list(text)
for i in range(len(text)):
    if text[i] == t1:
        text[i] = t2
    elif text[i] == t2:
        text[i] = t1
text = ''.join(text)
print(text)