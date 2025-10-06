from typing import List
def twoSum(numbers: List[int], target: int) -> List[int]:
    left = 0
    right = len(numbers) - 1
    current_sum = 0
    
    while left <= right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left + 1, right + 1]
        if current_sum > target:
            right -= 1
        else:
            left += 1
        
    return[-1, -1]

arr = [2,7,11,15]
target = 9
print(twoSum(arr, target))