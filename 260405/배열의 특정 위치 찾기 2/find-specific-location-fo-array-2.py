arr = list(map(int, input().split()))
odd = sum(arr[::2])
even = sum(arr[1::2])
if odd > even:
    print(f"{odd - even}")
elif odd < even:
    print(f"{even - odd}")