# need to return the index of peak element

def get_peak_element(nums : list[int]) -> int:
    if len(nums) == 1:
        return 0
    
    if nums[0] > nums[1]:
        return 0
    
    if nums[len(nums) - 1] > nums[len(nums) - 2]:
        return len(nums) - 1

    left, right = 1 , len(nums) - 2

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid - 1] < nums[mid] > nums[mid + 1]:
            return mid

        elif nums[mid - 1] > nums[mid]:
            right = mid - 1
        
        else:
            left = mid + 1
    
    return 0

if __name__ == "__main__":
                        # index 
    nums_1 = [1,2,3,1]  # o/p = 2
    nums_2 = [1,2,3,4]  # o/p = 3
    nums_3 = [4,3,2,1]  # o/p = 0
    nums_4 = [1]        # o/p = 0
    nums_5 = [1,2]      # o/p = 1

    print(get_peak_element(nums_1))
    print(get_peak_element(nums_2))
    print(get_peak_element(nums_3))
    print(get_peak_element(nums_4))
    print(get_peak_element(nums_5))
    