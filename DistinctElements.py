def removeDuplicates(nums: int) -> int:
    write = 0
    read = 1

    while read < len(nums):
        if nums[write] != nums[read]:
            write += 1
            nums[write] = nums[read]
        read += 1
    
    return write + 1

nums = [0,0,1,1,2,2,3,4,4,5,3]
print(removeDuplicates(nums))