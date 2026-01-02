def repeatedNTimes(nums: int) -> int:
    rep = len(nums) // 2

    nums_set = {}
    for num in nums:
        if num in nums_set:
            nums_set[num] += 1
        
        else:
            nums_set[num] = 1
        
    for key, value in nums_set.items():
        if value == rep:
            return key
        

nums = [1,2,3,2]
result = repeatedNTimes(nums)
print(result)