
def searchRange(nums: int, target: int) -> int:
    def get_lower_bound(nums, target):
        left = 0
        right = len(nums) - 1
        result = len(nums)

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        return result
    
    def get_upper_bound(nums, target):
        left = 0
        right = len(nums) - 1
        result = len(nums)

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        return result

    start_index, end_index = get_lower_bound(nums, target),get_upper_bound(nums, target) - 1
    
    if start_index == len(nums) or nums[start_index] != target:
        return [ -1 , -1 ]
    
    return [start_index, end_index]
