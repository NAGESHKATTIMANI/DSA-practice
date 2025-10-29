from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums_dict = {}

        for index in range(len(nums)):
            if nums[index] in nums_dict:
                if abs(nums_dict[nums[index]] - index)<= k:
                    return True
                else:
                    nums_dict[nums[index]] = index

            else:
                nums_dict[nums[index]] = index

        return False

nums = [1,0,1,1]
target = 1

problem_obj = Solution()
print(problem_obj.containsNearbyDuplicate(nums, target))