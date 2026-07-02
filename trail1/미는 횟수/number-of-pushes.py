A = input()
B = input()
count = 0
for _ in A:
    if A == B:
        print(count)
        break
    A = A[-1] + A[0:-1]
    count += 1
if A != B:
    print(-1)