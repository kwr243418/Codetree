text = input()
text = list(text)
text[1] = 'a'
text[-2] = 'a'
text = ''.join(text)
print(text)