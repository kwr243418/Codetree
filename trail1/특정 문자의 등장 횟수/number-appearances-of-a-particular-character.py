text = input()
countee = 0
counteb = 0
for i in range(0,len(text)-1,1):
    if text[i:i+2] == "ee":
        countee += 1
    if text[i:i+2] == "eb":
        counteb += 1
print(countee, counteb)
