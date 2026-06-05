text = input()
index = text.find('e')
text = text[0:index]+text[index+1:]
print(text)