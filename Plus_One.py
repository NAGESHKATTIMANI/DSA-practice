from typing import List
def plusOne( digits: List[int]) -> List[int]:
    carry = 1

    for index in range(len(digits)-1 , -1, -1):
        if digits[index] + 1 > 9:
            digits[index] = 0
            carry = 1
        
        else:
            digits[index] += 1
            carry = 0
        
        
        if carry == 1:
            nums = [0] * (len(digits) + 1)
            nums[0] = carry
            for index in range(1, len(nums)):
                nums[index] = digits[index - 1]
    
            return nums

nums = [9]
print(plusOne(nums))