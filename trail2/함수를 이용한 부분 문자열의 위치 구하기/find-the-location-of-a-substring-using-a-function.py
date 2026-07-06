text = input()
pattern = input()

# Please write your code here.
def findidx():
    for i in range(len(text)):
        if text[i:i+len(pattern)] == pattern[::]:
            return i
    return -1


print(findidx())