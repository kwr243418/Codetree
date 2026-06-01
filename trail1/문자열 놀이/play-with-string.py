S, Q = map(str, input().split())
S = list(S)
Q = int(Q)
arr = []
for _ in range(Q):
    arr.append(input().split())

for i in range(Q):
    if arr[i][0] == '1':
        S[int(arr[i][1])-1], S[int(arr[i][2])-1] = S[int(arr[i][2])-1], S[int(arr[i][1])-1]
        S = ''.join(S)
        print(S)
        S = list(S)
    elif arr[i][0] == '2':
        for j in range(len(S)):
            if S[j] == arr[i][1]:
                S[j] = arr[i][2]
        S = ''.join(S)
        print(S)
        S = list(S)
