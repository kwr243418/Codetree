count = 0
arr = []
while True:
    text = input()
    if text == '0':
        break
    count += 1
    if count % 2 == 1:
        arr.append(text)
print(count)
for i in arr:
    print(i)