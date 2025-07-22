from typing import List

def threeSum(nums):
    nums.sort()  # Sort the array
    result = []

    for i in range(len(nums)):
        # Skip duplicate values for the first number
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        target = -nums[i]
        left, right = i + 1, len(nums) - 1

        # Two-pointer approach
        while left < right:
            current_sum = nums[left] + nums[right]

            if current_sum == target:
                result.append([nums[i], nums[left], nums[right]])

                # Skip duplicates on both ends
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                # Move both pointers
                left += 1
                right -= 1

            elif current_sum < target:
                left += 1
            else:
                right -= 1

    return result

nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))