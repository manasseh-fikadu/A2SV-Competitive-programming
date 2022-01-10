t = int(input())
for i in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    for j in range(0, n-1):
        if nums[j] == nums[j+1]:
            nums[j] *= -1
        if j == n-1 and nums[j] == nums[j+1]:
            nums[j] *= -1
    print(len(set(nums)))
