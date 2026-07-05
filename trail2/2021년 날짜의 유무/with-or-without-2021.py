M, D = map(int, input().split())

# Please write your code here.
def isin2021(M, D):
    if not 1 <= M <= 12:
        return False
    md = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if 1 <= D <= md[M-1]:
        return True
    else:
        return False


if isin2021(M, D):
    print("Yes")
else:
    print("No")