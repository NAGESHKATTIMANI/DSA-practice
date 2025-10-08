
# Approach 1 
# the above algo is solved without using any data structure
# TC : O(N)
# SC : O(1)
def containsDuplicate( nums: list[int]) -> bool:
    nums = sorted(nums)
    index_1 = 0
    index_2 = 1
    while index_2 < len(nums):
        if nums[index_1] != nums[index_2]:
            index_2 += 1
            index_1 += 1
        else:
            return False
    return True

nums = [1,2,3,1]
print(containsDuplicate(nums))

# Approach 2 :
# using set 

def containsDuplicate_v2( nums: list[int]) -> bool:
    seen = set()
    for num in nums:
        if num not in seen:
            seen.add(num)
        else:
            return False
    return True

nums = [1,2,3,1]
print(containsDuplicate_v2(nums))


# approach 3 
# checking the length and returning the output

def containsDuplicate_v3( nums: list[int]) -> bool:
    if len(set(nums)) == len(nums):
        return True
    else:
        return False
    
nums = [1,2,3,1]
print(containsDuplicate_v3(nums))