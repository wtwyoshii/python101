def move(nums):
    last_non_zero = 0
    n = len(nums)


    for i in range(n):
        if nums[i] != 0:
            nums[last_non_zero] = nums[i]
            last_non_zero += 1

    for i in range(last_non_zero, n):
        nums[i] = 0

nums = [0 ,1,0, 3, 12]
move(nums)
print(nums)