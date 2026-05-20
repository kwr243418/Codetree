a, b = map(str, input().split())

if len(a) > len(b):
    print(a, len(a))
elif len(a) < len(b):
    print(b, len(b))
elif len(a) == len(b):
    print("same")