n = int(input())
price = list(map(int, input().split()))
arr = []
# Please write your code here.
for i in range(n):
    for j in range(i+1,n):
        if price[j] - price[i] > 0:
            arr.append(price[j] - price[i])
if len(arr) > 0:
    max = arr[0]
    for i in arr:
        if max < i:
            max = i
    print(max)
else :
    print(0)