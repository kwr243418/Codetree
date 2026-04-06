n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
idx = n
while idx > 0:
    max = nums[0]
    for i in range(len(nums[:idx])):
        if max < nums[i]:
            max = nums[i]
    idx = nums.index(max)
    print(idx + 1, end=" ")