def removeDuplicates(nums):
    n = len(nums)
    pos = 0
    for i in range(n):
        if pos < 2 or nums[i] != nums[pos - 2]:
            nums[pos] = nums[i]
            pos += 1
    return pos

nums = [1 , 1 , 1 , 2, 2, 3]
length = removeDuplicates(nums)
print(length)
print(nums[:length])