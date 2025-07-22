def remove(nums, val):
    write = 0
    for read in range(len(nums)):
        if nums[read] != val:
            nums[write] = nums[read]
            write += 1
    return write
    
nums = [3, 2, 2, 3]
val = 3

new_length = remove(nums, val)
print(new_length)
print(nums[:new_length])