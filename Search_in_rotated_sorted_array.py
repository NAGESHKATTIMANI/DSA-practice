def search(nums: list[int], target: int) -> bool:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return True
        
        if nums[left]  == nums[mid]:
            left += 1
            continue

        elif nums[mid] > nums[left]:
            if nums[left] <= target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        else:
            if nums[mid] <= target <= nums[right]:
                left = mid + 1
            else:
                right = mid -1

    return False 

nums = [1,0,1,1,1]
target = 0
print(search(nums, target))