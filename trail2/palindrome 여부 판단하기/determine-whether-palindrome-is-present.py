A = input()

# Please write your code here.
def palindrome(arr):
    n = len(arr)
    if n % 2 == 0:
        if arr[0:int(n/2):1] == arr[n:int(n/2)-1:-1]:
            print("Yes")
        else:
            print("No")
    else:
        if arr[0:int(n/2):1] == arr[n:int(n/2):-1]:
            print("Yes")
        else:
            print("No")


palindrome(A)