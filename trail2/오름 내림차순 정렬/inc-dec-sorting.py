n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
nums.sort()
for i in range(n):
    print(nums[i], end=' ')
print()
for i in range(n-1,-1,-1):
    print(nums[i], end=' ')