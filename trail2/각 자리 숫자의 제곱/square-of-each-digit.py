N = int(input())

# Please write your code here.
def sqs(n):
    if n < 10:
        return n * n
    return sqs(n//10) + ((n%10) * (n%10))


print(sqs(N))