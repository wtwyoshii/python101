def subarray(nums, target):
    n = len(nums)
    prefix = [0]*(n+1)

    for i in range(n):
        prefix[i+1] = prefix[i] + nums[i]

    for length in range(2, n + 1):
        for start in range(n - length + 1):
            end = start + length
            sub_sum = prefix[end] - prefix[start]
            if abs(sub_sum/length - target) < 1e-9:
                return True
    return False

nums = [1, 3, 2, 4, 7]
target = 3.0
result = subarray(nums, target)
print(result)

