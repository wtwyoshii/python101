def max_sum_k(nums, l):
    n = len(nums)

    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(k, n):
        window_sum = window_sum - nums[i-k] + nums[i]

        max_sum = max(max_sum, window_sum)

    return max_sum

nums = [2, 1, 5, 1, 3, 2]
k = 4
result = max_sum_k(nums, k)
print(result)
