a, b = map(int, input().split())

# Please write your code here.
def to_the_power_of_N(a, b):
    c = a
    for _ in range(1, b):
        c = c * a
    print(c)


to_the_power_of_N(a, b)